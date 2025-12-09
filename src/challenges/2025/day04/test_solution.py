"""Tests for Day 4: Printing Department"""

import pytest

from utils import read_lines

from .solution import (
    count_neighbours,
    get_accessible_rolls,
    iteratively_get_accessible_rolls,
    parse_rolls,
    solve,
)


@pytest.fixture
def example_grid(example_file):
    """Grid from example.txt."""
    return read_lines(example_file)


@pytest.fixture
def example_rolls(example_grid):
    """Parsed rolls from example grid."""
    return parse_rolls(example_grid)


class TestNeighborCount:
    """Test getting neighbors for paper rolls."""

    def test_corner_roll(self) -> None:
        """Test a roll in the corner with one neighbor."""
        grid = [
            "@@..",
            "....",
            "....",
            "....",
        ]
        rolls = parse_rolls(grid)
        assert count_neighbours(rolls, (0, 0)) == 1
        assert count_neighbours(rolls, (0, 1)) == 1

    def test_middle_roll_no_neighbors(self) -> None:
        """Test a roll with no neighbors."""
        grid = [
            "...",
            ".@.",
            "...",
        ]
        rolls = parse_rolls(grid)
        assert count_neighbours(rolls, (1, 1)) == 0

    def test_middle_roll_all_neighbors(self) -> None:
        """Test a roll surrounded by 8 neighbors."""
        grid = [
            "@@@",
            "@@@",
            "@@@",
        ]
        rolls = parse_rolls(grid)
        assert count_neighbours(rolls, (1, 1)) == 8

    def test_edge_roll(self) -> None:
        """Test a roll on the edge."""
        grid = [
            "...",
            "@@@",
            "...",
        ]
        rolls = parse_rolls(grid)
        assert count_neighbours(rolls, (1, 0)) == 1  # left edge
        assert count_neighbours(rolls, (1, 1)) == 2  # middle
        assert count_neighbours(rolls, (1, 2)) == 1  # right edge


class TestAccessibleRolls:
    """Test counting accessible paper rolls."""

    def test_example_from_problem(self) -> None:
        """Test the example grid from the problem statement."""
        grid = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        rolls = parse_rolls(grid)

        assert len(get_accessible_rolls(rolls)) == 13

    def test_single_roll(self) -> None:
        """Test a single roll is accessible."""
        grid = ["@"]
        rolls = parse_rolls(grid)

        assert len(get_accessible_rolls(rolls)) == 1

    def test_two_adjacent_rolls(self) -> None:
        """Test two adjacent rolls are both accessible."""
        grid = ["@@"]
        rolls = parse_rolls(grid)

        assert len(get_accessible_rolls(rolls)) == 2

    def test_cluster_of_four_rolls(self) -> None:
        """Test a 2x2 cluster where each has 3 neighbors (all accessible)."""
        grid = [
            "@@",
            "@@",
        ]
        rolls = parse_rolls(grid)

        assert len(get_accessible_rolls(rolls)) == 4

    def test_dense_cluster(self) -> None:
        """Test a 3x3 cluster where center has 8 neighbors (not accessible)."""
        grid = [
            "@@@",
            "@@@",
            "@@@",
        ]
        rolls = parse_rolls(grid)
        # Center has 8 neighbors (not accessible)
        # Corners have 3 neighbors (accessible)
        # Edges have 5 neighbors (not accessible)

        assert len(get_accessible_rolls(rolls)) == 4  # Only corners


class TestSolver:
    """Test the main solver function."""

    def test_solve_example(self) -> None:
        """Test solving the example."""
        grid = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        rolls = parse_rolls(grid)

        assert len(get_accessible_rolls(rolls)) == 13


class TestRemoveAccessibleRolls:
    """Test iterative removal of accessible rolls."""

    def test_example_from_problem(self) -> None:
        """Test the example from Part 2."""
        grid = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        rolls = parse_rolls(grid)
        assert iteratively_get_accessible_rolls(rolls) == 43

    def test_single_accessible_roll(self) -> None:
        """Test with a single accessible roll."""
        grid = ["@"]
        rolls = parse_rolls(grid)
        assert iteratively_get_accessible_rolls(rolls) == 1

    def test_two_connected_rolls(self) -> None:
        """Test with two connected rolls."""
        grid = ["@@"]
        rolls = parse_rolls(grid)
        # Both have 1 neighbor each, so both accessible initially
        # After removing one, the other has 0 neighbors and is removed
        assert iteratively_get_accessible_rolls(rolls) == 2

    def test_dense_cluster_cascading(self) -> None:
        """Test a dense 3x3 cluster where removal cascades."""
        grid = [
            "@@@",
            "@@@",
            "@@@",
        ]
        rolls = parse_rolls(grid)
        # Corners have 3 neighbors (accessible)
        # After corners removed, edges have 2-3 neighbors (accessible)
        # Eventually all get removed through cascading
        assert iteratively_get_accessible_rolls(rolls) == 9

    def test_cascading_removal(self) -> None:
        """Test that removal cascades properly."""
        grid = [
            "..@..",
            ".@@@.",
            "@@@@@",
            ".@@@.",
            "..@..",
        ]
        rolls = parse_rolls(grid)
        # Center has 4 neighbors (not accessible)
        # Cross pattern should cascade from outside to center
        assert iteratively_get_accessible_rolls(rolls) > 0


class TestSolverPart2:
    """Test the Part 2 solver."""

    def test_solve_part2_example(self) -> None:
        """Test Part 2 with the example."""
        grid = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        rolls = parse_rolls(grid)
        assert iteratively_get_accessible_rolls(rolls) == 43


class TestMain:
    """Test main entry point and solve function."""

    def test_solve_with_example(self, example_file):
        """Test solve function with example.txt."""
        part1, part2 = solve(example_file)
        assert part1 == 13
        assert part2 == 43

    def test_example_part1(self, example_rolls):
        """Test Part 1 with example data."""
        assert len(get_accessible_rolls(example_rolls)) == 13

    def test_example_part2(self, example_rolls):
        """Test Part 2 with example data."""
        assert iteratively_get_accessible_rolls(example_rolls.copy()) == 43
