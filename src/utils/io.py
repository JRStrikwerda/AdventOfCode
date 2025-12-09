"""Simple, efficient I/O utilities for Advent of Code."""

from collections.abc import Callable
from pathlib import Path


def read_input(filepath: str | Path, *, strip: bool = True) -> str:
    """Read entire input file as string."""
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")
    return content.strip() if strip else content


def read_lines(
    filepath: str | Path,
    *,
    skip_empty: bool = True,
    strip: bool = True,
    filter_fn: Callable[[str], bool] | None = None,
) -> list[str]:
    """Read input file as list of lines."""
    path = Path(filepath)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    if strip:
        lines = [line.strip() for line in lines]

    if skip_empty:
        lines = [line for line in lines if line]

    if filter_fn:
        lines = [line for line in lines if filter_fn(line)]

    return lines
