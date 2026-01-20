"""
Shelf class: a labelled list
"""


from typing import Any, Union, Optional, Dict, List

# A label is either str or int
LabelType = Union[str, int]

class Cell:
    "A cell is a mutable structure with two items: value and label"
    __slots__ = ('value', 'label')

    def __init__(self, value:Any, label:Optional[str]=None):
        self.value = value
        self.label = label

    def __repr__(self):
        return f"Cell(value={self.value!r}, label={self.label!r})"




class Shelf(list):
    """
    A shelf is a dual access stream, by index (int) and by label (str).
    In other words, it works both as a list and a dictionary.

    Iterating through a shelf returns the **values** as in a list.

    Internal implementation
    -----------------------
    It is implemented as a list of mutable cells (value, key).
    It has an attribute _cardfile (dictionary) that maps each key
    to each cell.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize Shelf with positional values and labeled values.

        - If a single dict is passed as the only arg → treated as labeled input
        - If a single list is passed as the only arg → treated as unlabeled input
        - Positional values (args) → appended as unlabeled cells
        - Keyword values (kwargs) → appended as labeled cells
        """
        super().__init__()
        self._cardfile: Dict[str, Cell] = {}

        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, Shelf):
                for cell in arg:
                    self.append(cell.value, label=cell.label)
                args = ()
            elif isinstance(arg, dict):
                for label, value in arg.items():
                    self.append(value, label=label)
                args = ()
            elif isinstance(arg, list):
                for value in arg:
                    self.append(value)
                args = ()
            else:
                raise TypeError(f"Object of class '{type(arg).__name__}' "
                                "cannot converted into a shelf.")


        for value in args:
            self.append(value)

        for label, value in kwargs.items():
            self.append(value, label=label)

    @classmethod
    def from_list(cls, values: List[Any]) -> "Shelf":
        """Construct Shelf from a list of unlabeled values."""
        if not isinstance(values, list):
            raise TypeError("from_list expects a list")
        shelf = cls()
        for value in values:
            shelf.append(value)
        return shelf

    @classmethod
    def from_dict(cls, mapping: Dict[str, Any]) -> "Shelf":
        """Construct Shelf from a dict of labeled values."""
        if not isinstance(mapping, dict):
            raise TypeError("from_dict expects a dict")
        shelf = cls()
        for label, value in mapping.items():
            shelf.append(value, label=label)
        return shelf



    # --------------------------------
    # List-type insertion (fundamental)
    # --------------------------------
    def __iter__(self):
        for cell in super().__iter__():
            yield cell.value

    def append(self, value, label:Optional[str]=None):
        cell = Cell(value, label)
        super().append(cell)
        if label:
            if label in self._cardfile:
                raise ValueError(f"Duplicate label: {label}")
            self._cardfile[label] = cell

    def update(self, mapping: Dict[str, Any]) -> None:
        "Bulk update labeled cells"
        for label, value in mapping.items():
            if label in self._cardfile:
                self._cardfile[label].value = value
            else:
                cell = Cell(value, label)
                self.append(cell)
                self._cardfile[label] = cell



    # --------------------------------
    # Common list/dict access and update methods
    # --------------------------------
    def __getitem__(self, key: LabelType):
        if isinstance(key, int):
            return super().__getitem__(key).value
        elif isinstance(key, str):
            return self._cardfile[key].value
        raise TypeError("Key must be int or str")

    def __setitem__(self, key: LabelType, value):
        if isinstance(key, int):
            cell = super().__getitem__(key)
            cell.value = value
        elif isinstance(key, str):
            if key in self._cardfile:
                # exists
                self._cardfile[key].value = value
            else:
                # doesn't exist
                self.append(value, key)
        else:
            raise TypeError("Key must be int or str")

    def __delitem__(self, key: LabelType):
        if isinstance(key, int):
            cell = super().__getitem__(key)
            super().__delitem__(key)
            if cell.label:
                self._cardfile.pop(cell.label, None)
        elif isinstance(key, str):
            cell = self._cardfile.pop(key)
            super().__delitem__(self.index(cell))
        else:
            raise TypeError("Key must be int or str")

    def __contains__(self, key: LabelType) -> bool:
        "Check if label or index exists"
        if isinstance(key, str):
            return key in self._cardfile
        return 0 <= key < len(self)


    def pop(self, key: LabelType = None, default: Any = None) -> Any:
        """
        Remove and return value by label, index, or last item.

        - If key is a str → remove by label
        - If key is an int → remove by index
        - If key is None → remove last item
        - If key is missing → return default
        """
        try:
            if key is None:
                cell = super().pop()
            elif isinstance(key, str):
                cell = self._cardfile.pop(key)
                self.remove(cell)
            else:
                cell = super().pop(key)
                if cell.label is not None:
                    self._cardfile.pop(cell.label, None)
            return cell.value
        except (KeyError, IndexError):
            return default

    # ---------------------
    # Dict-specific methods
    # ---------------------

    def get(self, key: LabelType, default: Any = None) -> Any:
        "Safe retrieval by label or index"
        try:
            return self[key]
        except (KeyError, IndexError):
            return default

    def keys(self):
        "Yield ALL keys: labels if present, else indices"
        return (key for key, _ in self.items())


    def values(self):
        "Yield all cell values"
        return (value for value in self)
    
    def cells(self):
        """
        Yield all cells; this is useful for auditability

        ⚠️  Do not modify cell.label directly.
            Use `self.update[label] = value` to do so.
        """
        for cell in super().__iter__():
            yield cell

    def items(self):
        "Yield (key, value) pairs: label if present, else index"
        for i, cell in enumerate(super().__iter__()):
            key = cell.label if cell.label is not None else i
            yield key, cell.value



    def rename(self, old_label:str, new_label:str):
        """
        Rename means here "relabel a cell"
        (assuming the old label exists and the new label is not used yet).
        """
        if not isinstance(old_label, str) or not isinstance(new_label, str):
            raise KeyError("Labels must be str or int")
        if new_label in self._cardfile:
            raise KeyError(f"Label '{new_label}' already exists")
        try:
            cell = self._cardfile[old_label]
        except KeyError:
            raise KeyError(f"Label '{old_label}' not found")
        cell.label = new_label
        del self._cardfile[old_label]
        self._cardfile[new_label] = cell

    def update(self, mapping: Dict[str, Any]) -> None:
        "Bulk update labeled cells"
        for label, value in mapping.items():
            if label in self._cardfile:
                self._cardfile[label].value = value
            else:
                cell = Cell(value, label)
                self.append(cell)
                self._cardfile[label] = cell
    
    # ---------------------
    # Specific
    # ---------------------
    def get_label(self, index:int):
        "Get the label from the list index"
        return super().__getitem__(index).label

    def get_index(self, label:str):
        "Get the index from the label"
        return self.index(self._cardfile[label])
    
    def labels(self):
        "Yield all labels from labeled cells"
        return (cell.label for cell in self if cell.label is not None)

    
    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({list(self)}, cardfile={self._cardfile})"