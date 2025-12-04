# Advent of Code Solutions

Solutions for [Advent of Code](https://adventofcode.com) using Python 3.14.

## Structure

```
src/
├── utils/                  # Shared utilities
│   ├── __init__.py
│   └── io.py              # I/O functions
└── challenges/            # Year-based solutions
    └── 2025/              # 2025 solutions
        ├── day01/         # Day 1: Safe Dial
        ├── day02/         # Day 2: Gift Shop
        ├── day03/         # Day 3: Lobby
        └── day04/         # Day 4: Printing Department
```

## Setup

```bash
# Install UV (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
make install
```

## Quick Start

```bash
# Show all commands
make help

# Run solutions
make run                      # Runs all solutions
make run ARGS="--latest"      # Latest solution
make run ARGS="-y 2025"       # All 2025 solutions
make run ARGS="-y 2025 -d 1"  # Day 1 of 2025

# Direct execution
./run.py --latest             # Latest solution
./run.py -y 2025              # All 2025 solutions
./run.py -y 2025 -d 1         # Day 1 of 2025
./run.py --help               # Show all options

# Code quality
make format                   # Format code
make lint                     # Lint code (with auto-fix)
make test                     # Run tests
make test-cov                 # Tests with coverage
make check                    # Format + lint + test
```
