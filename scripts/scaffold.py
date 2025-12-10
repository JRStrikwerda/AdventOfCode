#!/usr/bin/env python3
"""
Scaffold a new Advent of Code solution directory with template files.
"""

import sys
from pathlib import Path


def create_solution_structure(year: int, day: int) -> None:
    """Create directory structure and template files for a new AoC solution."""
    # Create directory structure
    day_dir = Path(f"src/challenges/{year}/day{day:02d}")
    day_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    init_file = day_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("")

    # Create example.txt with template
    example_file = day_dir / "example.txt"
    if not example_file.exists():
        example_file.write_text("# Paste example input here\n")

    # Create input.txt with template
    input_file = day_dir / "input.txt"
    if not input_file.exists():
        input_file.write_text("# Paste puzzle input here\n")

    # Create solution.py with template
    solution_file = day_dir / "solution.py"
    if not solution_file.exists():
        solution_template = f'''"""
Advent of Code {year} - Day {day}: [Puzzle Title]
[Brief description]
"""

from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import read_lines


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    _lines = read_lines(filepath)

    # Part 1 solution
    part1 = 0

    # Part 2 solution
    part2 = 0

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)

    print(f"Part 1: {{part1}}")
    print(f"Part 2: {{part2}}")
'''
        solution_file.write_text(solution_template)

    # Create test_solution.py with template
    test_file = day_dir / "test_solution.py"
    if not test_file.exists():
        test_template = f'''"""Tests for Day {day}: [Puzzle Title]"""

from .solution import solve


def test_example(example_file):
    """Test with example input."""
    part1, part2 = solve(example_file)
    assert part1 == 0  # Update with expected value
    assert part2 == 0  # Update with expected value
'''
        test_file.write_text(test_template)

    print(f"✓ Created solution structure at {day_dir}")
    print(f"  - {example_file.name}")
    print(f"  - {input_file.name}")
    print(f"  - {solution_file.name}")
    print(f"  - {test_file.name}")
    print("\nNext steps:")
    print(f"  1. Add example input to {example_file}")
    print(f"  2. Add puzzle input to {input_file}")
    print("  3. Update puzzle title in solution.py and test_solution.py")
    print("  4. Implement solution logic")
    print("  5. Update test assertions with expected values")
    print(f"\nRun solution: make run ARGS='--year {year} --day {day}'")


def main() -> None:
    """Parse arguments and create solution structure."""
    if len(sys.argv) != 3:
        print("Usage: python scripts/scaffold.py <year> <day>")
        print("Example: python scripts/scaffold.py 2025 8")
        sys.exit(1)

    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])

        if day < 1 or day > 25:
            print("Error: Day must be between 1 and 25")
            sys.exit(1)

        create_solution_structure(year, day)

    except ValueError:
        print("Error: Year and day must be integers")
        sys.exit(1)


if __name__ == "__main__":
    main()
