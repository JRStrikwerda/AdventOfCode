"""
Advent of Code 2025 - Day 1: Safe Dial
Counts how many times a dial points at zero during rotations.
"""

from dataclasses import dataclass
from pathlib import Path

from utils import read_lines


@dataclass(frozen=True)
class Rotation:
    """A rotation instruction."""

    direction: str
    distance: int


class Dial:
    """Dial with circular arithmetic (0-99)."""

    def __init__(self, position: int = 50):
        self.position = position % 100

    def rotate(self, rotation: Rotation) -> int:
        """Apply rotation and return zero crossings during movement."""
        if rotation.distance == 0:
            return 0

        start = self.position
        distance = rotation.distance

        # Calculate new position
        if rotation.direction == "L":
            self.position = (self.position - distance) % 100
        else:
            self.position = (self.position + distance) % 100

        # Count zero crossings
        complete_cycles = distance // 100
        remaining = distance % 100

        if remaining > 0 and start != 0:
            if rotation.direction == "L":
                crosses = 1 if start < remaining and self.position != 0 else 0
            else:
                crosses = 1 if start + remaining >= 100 and self.position != 0 else 0
        else:
            crosses = 0

        return complete_cycles + crosses


def parse_rotation(line: str) -> Rotation:
    """Parse rotation from format 'L68' or 'R48'."""
    line = line.strip().upper()
    direction = line[0]
    if direction not in ("L", "R"):
        raise ValueError(f"Invalid direction: {direction}")
    return Rotation(direction, int(line[1:]))


def count_zeros(rotations: list[Rotation], count_during_rotation: bool) -> int:
    """
    Count times dial points at zero.

    Args:
        rotations: List of rotation instructions
        count_during_rotation: If True, count zeros during movement; if False, only at end positions
    """
    dial = Dial()
    count = 0
    for rotation in rotations:
        if count_during_rotation:
            count += dial.rotate(rotation)
        else:
            dial.rotate(rotation)
        if dial.position == 0:
            count += 1
    return count


def main() -> None:
    """Entry point."""
    input_file = Path(__file__).parent / "input.txt"
    rotations = [parse_rotation(line) for line in read_lines(input_file)]

    part1 = count_zeros(rotations, count_during_rotation=False)
    print(f"Part 1: {part1}")

    part2 = count_zeros(rotations, count_during_rotation=True)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
