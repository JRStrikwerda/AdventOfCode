from collections.abc import Callable, Iterable, Sequence
from typing import TypeVar

T = TypeVar("T")
Coordinate = tuple[int, int]
Line = tuple[Coordinate, Coordinate]
Grid = Sequence[Sequence[T]]


def map_range(range_str: str) -> tuple[int, int]:
    """Map a range specification string 'start-stop' to a tuple of integers (start, stop)."""
    start_str, stop_str = range_str.strip().split("-")
    return int(start_str), int(stop_str)


def map_coordinate(coord_str: str) -> Coordinate:
    """Map a coordinate specification string 'x,y' to a Coordinate tuple (x, y)."""
    x_str, y_str = coord_str.strip().split(",")
    return int(x_str), int(y_str)


def iterate_over_grid[T](
    grid: Grid, condition: Callable[[T], bool] | None = None
) -> Iterable[Coordinate]:
    """Iterate over a 2D grid and yield coordinates of elements satisfying the given condition."""
    return (
        (row_idx, col_idx)
        for row_idx, row in enumerate(grid)
        for col_idx, element in enumerate(row)
        if condition is None or condition(element)
    )


def get_grid_size(grid: Grid) -> tuple[int, int]:
    """Get the size of the grid as (number of rows, number of columns)."""
    return len(grid), len(grid[0])
