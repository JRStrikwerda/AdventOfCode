"""Shared pytest fixtures for all Advent of Code tests."""

from pathlib import Path

import pytest


@pytest.fixture
def example_file(request):
    """Path to example.txt in the test's directory."""
    return Path(request.fspath).parent / "example.txt"


@pytest.fixture
def input_file(request):
    """Path to input.txt in the test's directory."""
    return Path(request.fspath).parent / "input.txt"
