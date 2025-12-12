"""
Advent of Code 2025 - Day 9: Movie Theater
Find largest rectangles using red and green tiles.
"""

from dataclasses import dataclass, field
from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import read_lines


@dataclass
class Coordinate:
    """Represents a coordinate point."""

    x: int
    y: int


@dataclass
class Line:
    """Represents a horizontal or vertical line segment."""

    a: Coordinate
    b: Coordinate

    def __post_init__(self):
        """Ensure points are ordered."""
        if self.a.x > self.b.x or (self.a.x == self.b.x and self.a.y > self.b.y):
            self.a, self.b = self.b, self.a

    @property
    def is_horizontal(self) -> bool:
        return self.a.y == self.b.y


@dataclass(order=True)
class Rectangle:
    """Represents a rectangle defined by two corner points."""

    area: int
    a: Coordinate = field(compare=False)
    b: Coordinate = field(compare=False)

    def __post_init__(self):
        if self.a.x > self.b.x:
            self.a, self.b = self.b, self.a

    @property
    def interior(self) -> "Rectangle | None":
        """Get the interior rectangle (shrunk by 1 on all sides)."""
        x1 = min(self.a.x, self.b.x) + 1
        x2 = max(self.a.x, self.b.x) - 1
        y1 = min(self.a.y, self.b.y) + 1
        y2 = max(self.a.y, self.b.y) - 1

        # Check if interior has no area
        if x1 > x2 or y1 > y2:
            return None

        return Rectangle(
            area=(x2 - x1 + 1) * (y2 - y1 + 1),
            a=Coordinate(x1, y1),
            b=Coordinate(x2, y2),
        )

    def intersects_vertical_border(self, vertical_lines: list[Line]) -> bool:
        """Check if rectangle interior intersects any vertical border line."""
        interior = self.interior
        if interior is None:
            return False

        # Check vertical lines that could intersect
        for line in vertical_lines:
            if line.a.x < interior.a.x:
                continue
            if line.a.x > interior.b.x:
                break

            # Check if this vertical line crosses through the interior
            if (line.a.y <= interior.a.y <= line.b.y) or (line.a.y <= interior.b.y <= line.b.y):
                return True

        return False

    def intersects_horizontal_border(self, horizontal_lines: list[Line]) -> bool:
        """Check if rectangle interior intersects any horizontal border line."""
        interior = self.interior
        if interior is None:
            return False

        # Check horizontal lines that could intersect
        for line in horizontal_lines:
            if line.a.y < interior.a.y:
                continue
            if line.a.y > interior.b.y:
                break

            # Check if this horizontal line crosses through the interior
            if (line.a.x <= interior.a.x <= line.b.x) or (line.a.x <= interior.b.x <= line.b.x):
                return True

        return False

    def intersects_border(self, horizontal_lines: list[Line], vertical_lines: list[Line]) -> bool:
        """Check if rectangle intersects any border lines."""
        return self.intersects_vertical_border(vertical_lines) or self.intersects_horizontal_border(
            horizontal_lines
        )


def map_coordinate(coord_str: str) -> Coordinate:
    """Map a coordinate specification string 'x,y' to a Coordinate."""
    x_str, y_str = coord_str.strip().split(",")
    return Coordinate(int(x_str), int(y_str))


def calculate_area(a: Coordinate, b: Coordinate) -> int:
    """Calculate area of rectangle defined by two corner coordinates."""
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def create_border_lines(red_tiles: list[Coordinate]) -> tuple[list[Line], list[Line]]:
    """Create sorted lists of horizontal and vertical border lines."""
    horizontal_lines: list[Line] = []
    vertical_lines: list[Line] = []

    for i, a in enumerate(red_tiles):
        b = red_tiles[(i + 1) % len(red_tiles)]
        line = Line(a, b)
        if line.is_horizontal:
            horizontal_lines.append(line)
        else:
            vertical_lines.append(line)

    # Sort for efficient binary search
    horizontal_lines.sort(key=lambda line: line.a.y)
    vertical_lines.sort(key=lambda line: line.a.x)

    return horizontal_lines, vertical_lines


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    lines = read_lines(filepath)
    red_tiles = [map_coordinate(line) for line in lines]

    # Generate all rectangles sorted by area (descending)
    rectangles = [
        Rectangle(calculate_area(a, b), a, b)
        for i, a in enumerate(red_tiles)
        for b in red_tiles[i + 1 :]
    ]
    rectangles.sort(reverse=True)

    # Part 1: Find largest rectangle (any tiles)
    part1 = rectangles[0].area

    # Part 2: Find largest rectangle that doesn't cross border
    horizontal_lines, vertical_lines = create_border_lines(red_tiles)

    # Find first valid rectangle (largest that doesn't intersect border)
    part2 = 0
    for rect in rectangles:
        # Early exit if we can't beat current best
        if rect.area <= part2:
            break

        # Check if rectangle interior intersects border
        if not rect.intersects_border(horizontal_lines, vertical_lines):
            part2 = rect.area
            break

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
