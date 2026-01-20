from __future__ import annotations

from pathlib import PurePosixPath

from mkdocs_awesome_nav.nav.link import NavLink
from mkdocs_awesome_nav.nav.page import NavPage


class NavSection:
    def __init__(self, children: list[NavPage | NavLink | NavSection], *, path: PurePosixPath, title: str):
        self.children = children
        self.path = path
        self.title = title

    def to_mkdocs_config(self):
        return {self.title: [child.to_mkdocs_config() for child in self.children]}


class RootSection(NavSection):
    def to_mkdocs_config(self):
        return super().to_mkdocs_config()[self.title]
