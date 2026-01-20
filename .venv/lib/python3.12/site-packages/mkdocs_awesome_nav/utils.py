from pathlib import PurePosixPath
from typing import TypeVar

T = TypeVar("T")


def flatten_list(items: list[list[T] | T]) -> list[T]:
    result: list[T] = []
    for item in items:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def create_absolute_pattern(path: PurePosixPath, pattern: str) -> str:
    return (path / pattern).as_posix() + ("/" if pattern.endswith("/") else "")
