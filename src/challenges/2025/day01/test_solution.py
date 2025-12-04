"""Tests for Day 1: Safe Dial"""

import pytest

from .solution import Dial, Rotation, count_zeros, parse_rotation


class TestRotation:
    """Test Rotation value object."""

    def test_rotation_creation(self):
        rotation = Rotation("L", 68)
        assert rotation.direction == "L"
        assert rotation.distance == 68

    def test_rotation_immutable(self):
        rotation = Rotation("R", 48)
        with pytest.raises(AttributeError):
            rotation.distance = 50


class TestDialPosition:
    """Test Dial circular arithmetic."""

    def test_initial_position(self):
        dial = Dial(50)
        assert dial.position == 50

    def test_rotate_right_simple(self):
        dial = Dial(11)
        crossings = dial.rotate(Rotation("R", 8))
        assert dial.position == 19
        assert crossings == 0

    def test_rotate_left_simple(self):
        dial = Dial(19)
        crossings = dial.rotate(Rotation("L", 19))
        assert dial.position == 0
        assert crossings == 0

    def test_rotate_left_wraps_around(self):
        dial = Dial(5)
        crossings = dial.rotate(Rotation("L", 10))
        assert dial.position == 95
        assert crossings == 1

    def test_rotate_right_wraps_around(self):
        dial = Dial(95)
        crossings = dial.rotate(Rotation("R", 5))
        assert dial.position == 0
        assert crossings == 0

    def test_rotate_right_from_99(self):
        dial = Dial(99)
        crossings = dial.rotate(Rotation("R", 1))
        assert dial.position == 0
        assert crossings == 0

    def test_rotate_left_from_0(self):
        dial = Dial(0)
        crossings = dial.rotate(Rotation("L", 1))
        assert dial.position == 99
        assert crossings == 0

    def test_rotate_right_crosses_zero(self):
        dial = Dial(50)
        crossings = dial.rotate(Rotation("R", 60))
        assert dial.position == 10
        assert crossings == 1

    def test_rotate_left_crosses_zero(self):
        dial = Dial(50)
        crossings = dial.rotate(Rotation("L", 68))
        assert dial.position == 82
        assert crossings == 1

    def test_rotate_right_multiple_cycles(self):
        dial = Dial(50)
        crossings = dial.rotate(Rotation("R", 1000))
        assert dial.position == 50
        assert crossings == 10

    def test_is_at_zero(self):
        dial = Dial(0)
        assert dial.position == 0

        dial = Dial(50)
        assert dial.position == 50


class TestRotationParser:
    """Test rotation parsing."""

    def test_parse_left_rotation(self):
        rotation = parse_rotation("L68")
        assert rotation.direction == "L"
        assert rotation.distance == 68

    def test_parse_right_rotation(self):
        rotation = parse_rotation("R48")
        assert rotation.direction == "R"
        assert rotation.distance == 48

    def test_parse_with_whitespace(self):
        rotation = parse_rotation("  L30  ")
        assert rotation.direction == "L"
        assert rotation.distance == 30

    def test_parse_lowercase(self):
        rotation = parse_rotation("r14")
        assert rotation.direction == "R"
        assert rotation.distance == 14

    def test_parse_invalid_direction(self):
        with pytest.raises(ValueError):
            parse_rotation("X10")

    def test_parse_invalid_distance(self):
        with pytest.raises(ValueError):
            parse_rotation("Labc")


class TestSolution:
    """Test solution functions."""

    def test_example_part1(self):
        """Test Part 1 with example."""
        rotations = [
            Rotation("L", 68),
            Rotation("L", 30),
            Rotation("R", 48),
            Rotation("L", 5),
            Rotation("R", 60),
            Rotation("L", 55),
            Rotation("L", 1),
            Rotation("L", 99),
            Rotation("R", 14),
            Rotation("L", 82),
        ]

        password = count_zeros(rotations, count_during_rotation=False)
        assert password == 3

    def test_example_part2(self):
        """Test Part 2 with example."""
        rotations = [
            Rotation("L", 68),
            Rotation("L", 30),
            Rotation("R", 48),
            Rotation("L", 5),
            Rotation("R", 60),
            Rotation("L", 55),
            Rotation("L", 1),
            Rotation("L", 99),
            Rotation("R", 14),
            Rotation("L", 82),
        ]

        password = count_zeros(rotations, count_during_rotation=True)
        assert password == 6

    def test_no_zeros(self):
        """Test when dial never points at zero."""
        rotations = [
            Rotation("R", 10),
            Rotation("L", 5),
        ]

        password = count_zeros(rotations, count_during_rotation=False)
        assert password == 0

    def test_all_zeros(self):
        """Test when dial starts at zero and points at zero after every rotation."""
        dial = Dial(0)
        rotations = [
            Rotation("R", 100),
            Rotation("L", 200),
        ]

        count = 0
        for rotation in rotations:
            dial.rotate(rotation)
            if dial.position == 0:
                count += 1

        assert count == 2

    def test_multiple_cycles_part2(self):
        """Test R1000 from 50 crosses zero 10 times."""
        rotations = [Rotation("R", 1000)]

        password = count_zeros(rotations, count_during_rotation=True)
        assert password == 10
