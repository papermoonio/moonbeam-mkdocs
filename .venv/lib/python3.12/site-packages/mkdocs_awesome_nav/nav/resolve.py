from operator import attrgetter
from typing import TypeVar, cast

from mkdocs_awesome_nav.nav.context import MkdocsFilesContext
from mkdocs_awesome_nav.nav.directory import NavDirectory
from mkdocs_awesome_nav.nav.link import NavLink
from mkdocs_awesome_nav.nav.page import NavPage
from mkdocs_awesome_nav.nav.pattern import NavPattern
from mkdocs_awesome_nav.nav.section import NavSection
from mkdocs_awesome_nav.utils import flatten_list

TInput = TypeVar("TInput", bound=NavPage | NavPattern | NavDirectory | NavLink | NavSection)
TResult = TypeVar("TResult", bound=NavPage | NavSection | NavLink)


def resolve_in_priority_order(items: list[TInput], context: MkdocsFilesContext) -> list[TResult]:
    queue = _create_resolve_queue(items)
    for to_resolve in sorted(queue, key=attrgetter("priority")):
        to_resolve.resolve(context)

    return _flatten_result(cast(list[TResult | list[TResult]], items))


def _create_resolve_queue(items: list[TInput]):
    for index, item in enumerate(items):
        if isinstance(item, NavSection):
            yield from _create_resolve_queue(item.children)
        elif isinstance(item, NavPage) or isinstance(item, NavDirectory) or isinstance(item, NavPattern):
            yield _ItemToBeResolved(item, result=items, result_index=index)


def _flatten_result(items: list[TResult | list[TResult]]):
    result = flatten_list(items)
    for item in result:
        if isinstance(item, NavSection):
            item.children = _flatten_result(cast(list[TResult | list[TResult]], item.children))
    return result


class _ItemToBeResolved:
    def __init__(
        self,
        item: NavPage | NavDirectory | NavPattern,
        result: list,
        result_index: int,
    ):
        self._item = item
        self._result = result
        self._result_index = result_index

    @property
    def priority(self):
        if isinstance(self._item, NavPage):
            return 1, self._result_index
        if isinstance(self._item, NavDirectory):
            return 2, -len(self._item.path.parts), self._result_index
        if isinstance(self._item, NavPattern):
            return 3, self._result_index

    def resolve(self, context: MkdocsFilesContext):
        self._result[self._result_index] = self._item.resolve(context)
