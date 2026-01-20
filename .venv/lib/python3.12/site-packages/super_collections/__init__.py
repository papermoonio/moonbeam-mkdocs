"""
Super Collections

Their purpose is to turn complex input such as json or YAML files into
Python objects accessible with attributes, and self documented.

The general idea is that those structured files are combinations
of lists and dictionaries.

(C) Laurent Franceschetti 2024
"""
import datetime
import json
import inspect
from typing import Any, Union, Optional, Dict
from abc import ABC, abstractmethod


import hjson

from .shelf import Shelf, Cell # makes import easier

# -------------------------------------
# Low-level fixtures
# -------------------------------------
from collections import UserDict, deque

DICT_TYPES = dict, UserDict

class JSONEncoder(json.JSONEncoder):
    """
    Custom encoder for JSON serialization.
    Used for debugging purposes.

    It's purpose is to be extremely reliable.
    """
    def default(self, obj: Any) -> Any:
        TIME_FORMATS = (datetime.datetime, datetime.date, datetime.time)
        if isinstance(obj, TIME_FORMATS):
            return obj.isoformat()
        elif isinstance(obj, UserDict):
            # for objects used by some packages
            return dict(obj)
        elif inspect.isfunction(obj):
            return f"Function: %s %s" % (inspect.signature(obj),
                                        obj.__doc__)
        try:
            return super().default(obj)
        except TypeError:
            pass

        # It all else fails, output as best as I can
        # If the object wants to speak for itself, I’ll let it. If it can’t, I’ll describe it.
        try:
            return str(obj)
        except Exception:
            pass
        try:
            return repr(obj)
        except Exception:
            # If all else fails, return the object's type
            return f"<OBJECT {type(obj).__name__}>"



def json_encode(obj) -> str:
    """
    Encode a json string with the encoder.

    To be used for debugging purposes.
    """
    return json.dumps(obj, cls=JSONEncoder)


def yaml_support():
    """
    Support yaml format: registers YAML representers for SuperDict and SuperList.

    Ensures they serialize as _standard_ dicts and lists.
    Registers with both SafeDumper and Dumper for compatibility.
    Gracefully fails if PyYAML is not installed.
    """
    try:
        import yaml
    except ImportError as e:
        raise ImportError(
            "YAML support requires PyYAML. Please install it with `pip install pyyaml`."
        ) from e

    from . import SuperDict, SuperList  # local import to avoid circularity

    def plain_dict(dumper, data):
        return dumper.represent_dict(dict(data))

    def plain_list(dumper, data):
        return dumper.represent_list(list(data))

    for Dumper in (yaml.SafeDumper, yaml.Dumper):
        Dumper.add_representer(SuperDict, plain_dict)
        Dumper.add_representer(SuperList, plain_list)



def is_elementary_type(t):
    """
    Defines an elementary type in Python (str, int, etc.).

    An elementary type is defined as a type that is treated as a value
    (does not need to be broken down).
    
    Do not confuse this with an atomic type, which cannot be subdivided
    in Python.
    """
    return (not hasattr(t, '__dict__') and 
            not isinstance(t, (list, dict, tuple, set))
            )




# -------------------------------------
# Collections
# -------------------------------------

class SuperDict(dict):
    """
    A dictionary with keys accessible as properties
    (with the dot notation)

    a['foo'] <=> a.foo

    As a rule, the Superdict will expose as properties
    all keys that:

    1. Are valid identifiers
    2. Are not a standard property or method of the dict, 
        class notably:
        attributes, clear, copy, fromkeys, get, items,
        keys, pop, popitem, setdefault, update, values

    Lists in a SuperDict are converted into SuperLists, whose elements
    are in turn converted, etc...
    """

    def __init__(self, *args, **kwargs):
        # Call the superclass's __init__ method
        try:
            super().__init__(*args, **kwargs)
        except TypeError:
            # try to interpret:
            obj = get_dict(args[0])
            super().__init__(obj)
        self.__post_init__()

    def __post_init__(self):
        "Recursively transform sub-dictionary"
        for key, value in self.items():
            if isinstance(value, SUPER_TYPES):
                pass
            elif isinstance(value, DICT_TYPES):
                self[key] = SuperDict(value)
            elif isinstance(value, list):
                self[key] = SuperList(value)

    def __getattr__(self, name:str):
        "Allow dot notation on reading"
        ERR_MSG = "Cannot find attribute '%s'" % name
        try:
            return self[name]
        except KeyError:
            raise AttributeError(ERR_MSG)



    def properties(self):
        """
        Generate the valid properties
        (the dictionary keys that qualify as Python identifiers
        and are not callables)
        """
        return (item for item in self.keys() 
                if isinstance(item, str)
                    and item.isidentifier()
                    and not callable(getattr(self, item)))
    

    
    def __dir__(self):
        "List all attributes (for autocompletion, etc.)"
        return super().__dir__() + list(self.properties())
    
    # -------------------------------------
    # Output
    # -------------------------------------


    def __setattr__(self, name, value):
        "Allow dot notation on writing"
        # ERR_MSG = "Cannot assign an attribute starting with _ ('%s')" % name
        # if name.startswith('_'):
        #     raise AttributeError(ERR_MSG)     
        self[name] = value


    def update(self, other:dict):
        """
        Update the SuperDict with another.

        If necessary the other dictionary is converted into a SuperDict
        """
        if not isinstance(other, SuperDict):
            other = SuperDict(other)
        return super().update(other)
    
    
    # -------------------------------------
    # Output
    # -------------------------------------
    
    def to_json(self):
        """
        Convert to json.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        return json.dumps(self, cls=JSONEncoder)
    
    def to_hjson(self):
        """
        Convert to hjson.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        python_dict = json.loads(self.to_json())
        return hjson.dumps(python_dict)


    def __str__(self):
        "Print a superdict"
        return self.to_hjson()
    
    def __rich__(self):
        "Print a superdict (for rich)"
        r = [f"[bold red]{self.__class__.__name__}:[/]"]
        r.append(self.to_hjson())
        return("\n".join(r))       




class SuperList(list):
    """
    A list that supports the SuperDict,
    to allow recursion within complex structures
    """

    def __init__(self, *args, **kwargs):
        # Call the superclass's __init__ method
        super().__init__(*args, **kwargs)
        self.__post_init__()

    def __post_init__(self):
        "Recursively transform sub-list"
        for index, value in enumerate(self):
            if isinstance(value, SUPER_TYPES):
                pass
            elif isinstance(value, DICT_TYPES):
                self[index] = SuperDict(value)
            elif isinstance(value, list):
                self[index] = SuperList(value)



    # -------------------------------------
    # Modify
    # -------------------------------------

    def extend(self, l):
        "Extend the list with another one (transforms it first in SuperList)"
        l = SuperList(l)
        super().extend(l)

    def __add__(self, l):
        "Addition with another list"
        l = SuperList(l)
        return SuperList(super().__add__(l))
    # -------------------------------------
    # Output
    # -------------------------------------
    
    def to_json(self):
        """
        Convert to json.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        return json.dumps(self, cls=JSONEncoder)
    
    def to_hjson(self):
        """
        Convert to hjson.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        python_dict = json.loads(self.to_json())
        return hjson.dumps(python_dict)


    def __str__(self):
        "Print a superdict"
        return self.to_hjson()
    
    def __rich__(self):
        "Print a superdict (for rich)"
        r = [f"[bold red]{self.__class__.__name__}:[/]"]
        r.append(self.to_hjson())
        return("\n".join(r))     

SUPER_TYPES = SuperDict, SuperList

# -------------------------------------
# Factory function
# -------------------------------------

from collections.abc import Sequence


LIST_TYPES = 'ndarray', 'Series'

def get_list(obj:Any) -> list:
    """
    Get list from various objects.

    It is the default choice.
    It will raise a TypeError if a dict would be probably better suited.
    """
    if isinstance(obj, Sequence):
        # this includes lists proper
        return list(obj)
    elif isinstance(obj, (set, deque)):
        # Non-sequence standard types that also work
        return list(obj)    
    elif type(obj).__name__ in LIST_TYPES:
        # We name check those ones
        return list(obj)
    else:
        raise TypeError(f"Objects of type '{type(obj).__name__}' are not lists")


def get_dict(obj: Any) -> Dict[str, object]:
    """
    Extract a dictionary from various object types using introspection only.

    NOTE: We do not do __dict__, because it's too general and it might take
          a subclass of list.
    """

    try:
        return dict(obj)
    except TypeError:
        pass

    # 1. Custom .asdict() method
    if hasattr(obj, "asdict") and callable(getattr(obj, "asdict")):
        try:
            result = obj.asdict()
            if isinstance(result, dict):
                return result
        except Exception:
            pass

    # 2. .dict() method (e.g. Pydantic)
    if hasattr(obj, "dict") and callable(getattr(obj, "dict")):
        try:
            result = obj.dict()
            if isinstance(result, dict):
                return result
        except Exception:
            pass

    # 3. .dump() method (e.g. Marshmallow)
    if hasattr(obj, "dump") and callable(getattr(obj, "dump")):
        try:
            result = obj.dump()
            if isinstance(result, dict):
                return result
        except Exception:
            pass

    # 5. Dataclass fallback
    try:
        from dataclasses import is_dataclass, asdict
        if is_dataclass(obj):
            return asdict(obj)
    except ImportError:
        pass
    except Exception:
        pass

    # 6. No solution: raise an error
    raise TypeError(f"Cannot convert of type {obj.__class__.__name__}")


# These types could be considered as lists but are not
SPECIAL_ELEMENTARY_TYPES = str, bytes, bytearray

def super_collect(obj:Any) -> Union[SuperDict, SuperList]:
    """
    Factory function:
    Read an object and dispatch it into either a SuperDict or a SuperList
    """
    if isinstance(obj, SPECIAL_ELEMENTARY_TYPES):
        raise TypeError(f"Objects of type '{type(obj).__name__}' "
                        "are not accepted (elementary types)")
    try:
        list_obj = get_list(obj)
        return SuperList(list_obj)
    except TypeError:
        pass
    try:
        dict_obj = get_dict(obj)
        return SuperDict(dict_obj)
    except TypeError:
        raise TypeError(f"Cannot convert this object of type '{type(obj).__name__}'")



# -------------------------------------
# SuperShelf
# -------------------------------------

class SuperShelf(Shelf):
    """Shelf subclass that recursively wraps dicts and lists into SuperShelf."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            value = self._collect(value)
            self[key] = value

    def _collect(self, obj:Any) -> "SuperShelf":
        """
        Factory function:
        Read an object and make a SuperShelf
        """
        if is_elementary_type(obj):
            return obj
        if isinstance(obj, SuperShelf):
            return obj
        elif isinstance(obj, Shelf):
            return SuperShelf(obj)
        try:
            list_obj = get_list(obj)
            return SuperShelf(list_obj)
        except TypeError:
            pass
        try:
            dict_obj = get_dict(obj)
            return SuperShelf(dict_obj)
        except TypeError:
            pass
        raise TypeError(f"Cannot collect object of type '{type(obj).__name__}'")

    def append(self, value: Any, label: Optional[str] = None) -> None:
        """Append value to shelf, recursively wrapping containers."""
        if isinstance(value, dict) or isinstance(value, list):
            value = self._collect(value)
        super().append(value, label=label)


    @property
    def is_fully_collected(self) -> bool:
        """
        Validator predicate:
        Recursively checks whether this SuperShelf contains only:
        - elementary types
        - other SuperShelf instances that are themselves fully collected
        """
        for cell in self.cells():
            if not isinstance(cell, (SuperShelf, Cell)):
                # it's one or the other
                raise ValueError(f"{cell}: this is not a Supershelf or Cell, but {type(cell)}")
            elif is_elementary_type(cell.value):
                pass
            elif isinstance(cell.value, SuperShelf):
                if not cell.value.is_fully_collected:
                    return False
            else:
                return False
        return True





    # -------------------------------------
    # Keys as attributes
    # -------------------------------------
    def __getattr__(self, name:str):
        """
        Allow dot notation on reading keys, 
        e.g. foo.bar instead of foo['bar'].

        This is a CONVENIENCE method (for syntactic sugar) and it depends on:
        - the key being a valid Python identifier.
        - the attribute not being shadowed by an already existing one in the SuperShelf class.
        """
        ERR_MSG = "Cannot find attribute '%s'" % name
        try:
            return self[name]
        except KeyError:
            print("Predefined attributes:", list(vars(self).items()))
            print("Valid:", self.valid_names)
            print("Object type:", type(self).__name__)
            raise AttributeError(ERR_MSG)


    @property
    def _reserved_names(self):
        "Return the set of names reserved by the class or instance (methods, attributes)"
        return set(dir(type(self))) | set(self.__dict__)

    @property
    def valid_names(self):
        """
        Generate the valid names
        (the non-shadowed keys that qualify as Python identifiers)
        """
        return [
            item for item in self.keys()
            if isinstance(item, str)
            and item.isidentifier()
            and item not in self._reserved_names
        ]




    def find(self, key:str, value:Any):
        "Return the first item where getattr(item, key) == value (but skip elementary types)"
        for item in self:
            try:
                if getattr(item, key) == value:
                    return item
            except Exception:
                continue
        raise KeyError(f"Key '{key}' not found")

    # -------------------------------------
    # Output
    # -------------------------------------
    @property
    def _is_strict_list(self) -> bool:
        "Implementable as list (no labels)"
        return all(cell.label is None for cell in self.cells())

    @property
    def _is_strict_dict(self) -> bool:
        "Implementable as dictionary (all keys are labels)"
        return all(cell.label is not None for cell in self.cells())



    def to_json(self, *, indent: int = None) -> str:
        """
        Serialize the SuperCollection to a JSON string using the custom JSONEncoder.
        Each subcollection is optimized as a list, dict, or hybrid depending on addressing mode.

        Parameters:
            indent (int, optional): Number of spaces for pretty-printing. If None, output is compact.

        Returns:
            str: JSON string representing the serialized SuperCollection.
        """
        structure = [self._serialize_shelf(shelf) for shelf in self]
        return json.dumps(structure, indent=indent, cls=JSONEncoder)

    def _serialize_shelf(self, item) -> Any:
        """
        Serialize a single SuperShelf using the most compact representation:
        - As a list if all items are unlabelled
        - As a dict if all items are labelled
        - As a hybrid list of entries otherwise

        Parameters:
            shelf: A Shelf-like object supporting iteration and addressing mode predicates.

        Returns:
            A JSON-serializable structure (list or dict).
        """
        # print(f"Item: {item} -> {type(item).__name__}")
        if is_elementary_type(item):
            return item
        elif item._is_strict_list:
            return [self._serialize_cell(cell) for cell in shelf]
        elif item._is_strict_dict:
            return {cell.label: self._serialize_cell(cell) for cell in shelf}
        else:
            return [self._serialize_cell(cell) for cell in shelf]

    def _serialize_cell(self, cell) -> Any:
        """
        Serialize a single cell:
        - If labelled: as a singleton dict {label: value}
        - If unlabelled: as raw value
        Recursively serializes value if it supports .to_json().

        Parameters:
            cell: A Cell-like object with .label and .value attributes.

        Returns:
            A JSON-serializable value or singleton dict.
        """
        value = cell.value
        if hasattr(value, "to_json") and callable(value.to_json):
            value = value.to_json()
        return {cell.label: value} if cell.label is not None else value

    def to_hjson(self):
        """
        Convert to hjson.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        obj = json.loads(self.to_json())
        return hjson.dumps(obj)

    def __str__(self):
        "Print to hjson"
        return self.to_hjson()

    def __rich__(self):
        "Print (for rich)"
        r = [f"[bold red]{self.__class__.__name__}:[/]"]
        r.append(self.to_hjson())
        return("\n".join(r))      


# -------------------------------------
# Super Collection
# -------------------------------------
class SuperCollection(ABC):
    """
    The super collection abstract class
    """

    @staticmethod
    def collect(obj) -> Union[SuperDict, SuperList]:
        "The factory function"
        return super_collect(obj)
    
    @abstractmethod
    def to_json(self):
        """
        Convert to json.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.

        CAUTION: It must be reliable, so well tested.
        """
        pass

    @abstractmethod
    def to_hjson(self):
        """
        Convert to hjson.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        pass

    @abstractmethod
    def __str__(self):
        "Print (to hjson, in principle)"
        pass
    
    @abstractmethod
    def __rich__(self):
        "Print to the rich format"
        pass

SuperCollection.register(SuperList)
SuperCollection.register(SuperDict)
SuperCollection.register(SuperShelf)
