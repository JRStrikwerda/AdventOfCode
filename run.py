#!/usr/bin/env python3
"""Run Advent of Code solutions."""

import argparse
import re
from importlib import import_module
from pathlib import Path

CHALLENGES_DIR = Path(__file__).parent / "src" / "challenges"


def get_years() -> list[int]:
    """Get all available years."""
    if not CHALLENGES_DIR.exists():
        return []
    return sorted(int(p.name) for p in CHALLENGES_DIR.iterdir() if p.is_dir() and p.name.isdigit())


def get_days(year: int) -> list[int]:
    """Get all available days for a year."""
    year_path = CHALLENGES_DIR / str(year)
    if not year_path.exists():
        return []
    return sorted(
        int(re.search(r"\d+", p.name).group())
        for p in year_path.iterdir()
        if p.is_dir() and p.name.startswith("day")
    )


def run_solution(year: int, day: int, *, quiet: bool = False) -> None:
    """Run a specific day's solution by importing its module."""
    module_path = f"challenges.{year}.day{day:02d}.solution"

    try:
        if not quiet:
            print(f"\n{'=' * 60}")
            print(f"Day {day} - {year}")
            print(f"{'=' * 60}")
        module = import_module(module_path)
        if hasattr(module, "main"):
            module.main()
    except ModuleNotFoundError as e:
        msg = f"Solution not found: {module_path}\nError: {e}"
        raise SystemExit(msg) from e


def run_year(year: int) -> None:
    """Run all solutions for a given year."""
    days = get_days(year)

    if not days:
        raise SystemExit(f"No solutions found for year {year}")

    for day in days:
        run_solution(year, day)


def run_all() -> None:
    """Run all solutions for all years."""
    years = get_years()

    if not years:
        raise SystemExit("No solutions found")

    for year in years:
        run_year(year)


def main() -> None:
    """Parse arguments and run solutions."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s              Run all solutions
  %(prog)s -y 2025      Run all 2025 solutions
  %(prog)s -y 2025 -d 1 Run day 1 of 2025
  %(prog)s --latest     Run latest solution
        """,
    )
    parser.add_argument("-y", "--year", type=int, help="Year to run")
    parser.add_argument("-d", "--day", type=int, help="Day to run")
    parser.add_argument(
        "-l",
        "--latest",
        action="store_true",
        help="Run the latest available solution",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress headers",
    )

    args = parser.parse_args()

    # Handle --latest flag
    if args.latest:
        years = get_years()
        if not years:
            raise SystemExit("No solutions found")
        year = max(years)
        days = get_days(year)
        if not days:
            raise SystemExit(f"No solutions found for year {year}")
        day = max(days)
        run_solution(year, day, quiet=args.quiet)
        return

    # Handle year and day arguments
    if args.year and args.day:
        run_solution(args.year, args.day, quiet=args.quiet)
    elif args.year:
        run_year(args.year)
    elif args.day:
        # Day without year: use latest year
        years = get_years()
        if not years:
            raise SystemExit("No solutions found")
        run_solution(max(years), args.day, quiet=args.quiet)
    else:
        run_all()


if __name__ == "__main__":
    main()
