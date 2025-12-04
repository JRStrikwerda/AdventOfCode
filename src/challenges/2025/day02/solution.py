"""
Advent of Code 2025 - Day 2: Gift Shop
Finds invalid product IDs (repeated digit patterns).
"""

from pathlib import Path

from utils import read_input


def parse_ranges(filepath: Path) -> list[tuple[int, int]]:
    """Read and parse ranges from input file."""
    content = read_input(filepath)
    return [tuple(map(int, spec.strip().split("-"))) for spec in content.split(",") if spec.strip()]


def is_invalid_part1(product_id: int) -> bool:
    """
    Check if product ID is invalid (repeated pattern exactly twice).
    Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    s = str(product_id)
    mid = len(s) // 2
    return len(s) % 2 == 0 and s[:mid] == s[mid:]


def is_invalid_part2(product_id: int) -> bool:
    """
    Check if product ID is invalid (pattern repeated at least twice).
    Examples: 1111 (1 four times), 123123 (123 twice), 12341234 (1234 twice)
    """
    id_string = str(product_id)
    id_length = len(id_string)

    # Try all possible pattern lengths from 1 to length//2
    for pattern_length in range(1, id_length // 2 + 1):
        if id_length % pattern_length == 0:
            pattern = id_string[:pattern_length]
            if all(id_string[i] == pattern[i % pattern_length] for i in range(id_length)):
                return True
    return False


def sum_invalid_ids(ranges: list[tuple[int, int]], is_invalid: callable) -> int:
    """Sum all invalid product IDs across ranges using the given validation function."""
    total = 0
    for start, end in ranges:
        for product_id in range(start, end + 1):
            if is_invalid(product_id):
                total += product_id
    return total


def main() -> None:
    """Entry point."""
    input_file = Path(__file__).parent / "input.txt"
    ranges = parse_ranges(input_file)

    part1 = sum_invalid_ids(ranges, is_invalid_part1)
    print(f"Part 1: {part1}")

    part2 = sum_invalid_ids(ranges, is_invalid_part2)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
