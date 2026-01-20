from pathlib import PurePosixPath
from typing import Optional

from mkdocs.structure.files import File, Files, InclusionLevel


class Page:
    def __init__(self, file: File):
        self.path = PurePosixPath(file.src_uri)
        self.file = file


class Directory:
    def __init__(self, path: PurePosixPath, config_file: Optional[File]):
        self.path = path
        self.config_file = config_file


FileObject = Page | Directory


class MkdocsFilesContext:
    def __init__(self, mkdocs_files: Files, config_filename: str):
        self._mkdocs_files = mkdocs_files
        self._config_filename = config_filename

        self.root = self._create_directory(PurePosixPath("."))

        self._by_path: dict[PurePosixPath, FileObject] = dict()
        self.unvisited: set[FileObject] = set()

        for file in self._mkdocs_files.documentation_pages(inclusion=InclusionLevel.is_in_nav):
            page = Page(file)
            self._add_file_object(page)

            for parent_path in page.path.parents:
                if parent_path not in self._by_path:
                    directory = self._create_directory(parent_path)
                    self._add_file_object(directory)

    def get_by_path(self, path: PurePosixPath) -> Optional[FileObject]:
        # we go through get_file_from_path because the i18n plugin overrides it to resolve file.md into file.en.md
        mkdocs_file = self._mkdocs_files.get_file_from_path(path.as_posix())
        if mkdocs_file is not None:
            return self._by_path.get(PurePosixPath(mkdocs_file.src_uri), None)
        return self._by_path.get(path, None)

    def visit(self, item: FileObject) -> None:
        if item in self.unvisited:
            self.unvisited.remove(item)

    def _add_file_object(self, file_object: FileObject):
        self._by_path[file_object.path] = file_object
        self.unvisited.add(file_object)

    def _create_directory(self, path: PurePosixPath):
        config_file_path = path / self._config_filename
        config_file = self._mkdocs_files.get_file_from_path(config_file_path.as_posix())
        return Directory(path, config_file)
