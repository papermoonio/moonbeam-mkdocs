from __future__ import annotations

from typing import Optional

from mkdocs_awesome_nav.nav.context import MkdocsFilesContext, Page


class NavPage:
    def __init__(self, page: Page, *, title: Optional[str] = None):
        self.page = page
        self.title = title

    def resolve(self, context: MkdocsFilesContext) -> NavPage:
        context.visit(self.page)
        return self

    def to_mkdocs_config(self):
        path = self.page.path.as_posix()

        if self.title:
            return {self.title: path}

        return path
