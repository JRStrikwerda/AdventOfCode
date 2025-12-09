"""
Advent of Code 2025 - Day 6: Trash Compactor
Parse and solve Cephalopod Math Problems arranged in a grid format.
"""

from collections.abc import Callable
from itertools import zip_longest
from math import prod
from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import read_lines


def parse_operators(operator_line: str) -> list[Callable]:
    """Parse operator line into list of callable functions."""
    return [{"+": sum, "*": prod}[op] for op in operator_line if op in "+*"]


def parse_problems(lines: list[str]) -> list[list[str]]:
    """Parse input into problems by finding separator columns.
    Problems are separated by columns where all rows have spaces.
    """
    separators = [i for i in range(len(lines[0])) if all(row[i].isspace() for row in lines)]
    ranges = zip([-1, *separators], [*separators, len(lines[0])], strict=False)
    return [[row[start + 1 : end] for row in lines] for start, end in ranges if end > start + 1]


def extract_numbers(problem: list[str]) -> list[int]:
    """Extract numbers from problem rows, filtering out empty entries."""
    return [
        int("".join(d for d in row if d != " ")) for row in problem if any(d != " " for d in row)
    ]


def transpose_right_aligned(problems: list[list[str]]) -> list[list[str]]:
    """Transpose problems with right alignment for Part 2."""
    return [["".join(col) for col in zip_longest(*problem, fillvalue=" ")] for problem in problems]


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    *value_lines, operator_line = read_lines(filepath, strip=False)

    problems = parse_problems(value_lines)
    operators = parse_operators(operator_line)

    # Part 1: Read left-to-right, top-to-bottom
    part1 = sum(op(extract_numbers(prob)) for prob, op in zip(problems, operators, strict=True))

    # Part 2: Transpose to read right-to-left by digit columns
    transposed = transpose_right_aligned(problems)
    part2 = sum(op(extract_numbers(prob)) for prob, op in zip(transposed, operators, strict=True))

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
