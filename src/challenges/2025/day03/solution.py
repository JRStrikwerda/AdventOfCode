"""
Advent of Code 2025 - Day 3: Lobby
Find maximum joltage from battery banks.
"""

from pathlib import Path

from utils import read_lines


def find_max_joltage_part1(bank: str) -> int:
    """
    Find the maximum joltage by selecting two batteries from a bank.
    Batteries maintain their positions - we find the pair that forms the largest number.
    """
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage


def find_max_joltage_part2(bank: str, num_batteries: int = 12) -> int:
    """
    Find the maximum joltage by selecting exactly num_batteries from a bank.
    Strategy: Remove digits greedily to maximize the resulting number.
    This is the "remove k digits to get maximum number" problem.
    """
    digits_to_remove = len(bank) - num_batteries
    stack = []

    for digit in bank:
        # Remove smaller digits from the end while we can
        while stack and digits_to_remove > 0 and stack[-1] < digit:
            stack.pop()
            digits_to_remove -= 1
        stack.append(digit)

    # If we still need to remove digits, remove from the end
    while digits_to_remove > 0:
        stack.pop()
        digits_to_remove -= 1

    result = "".join(stack)
    return int(result)


def solve_part1(banks: list[str]) -> int:
    """Calculate total output joltage from all battery banks (2 batteries each)."""
    return sum(find_max_joltage_part1(bank) for bank in banks)


def solve_part2(banks: list[str]) -> int:
    """Calculate total output joltage from all battery banks (12 batteries each)."""
    return sum(find_max_joltage_part2(bank) for bank in banks)


def main() -> None:
    """Entry point."""
    input_file = Path(__file__).parent / "input.txt"
    banks = read_lines(input_file)

    part1 = solve_part1(banks)
    print(f"Part 1: {part1}")

    part2 = solve_part2(banks)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
