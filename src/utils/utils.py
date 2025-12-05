def map_range(range_str: str) -> tuple[int, int]:
    """Map a range specification string 'start-stop' to a tuple of integers (start, stop)."""
    start_str, stop_str = range_str.strip().split("-")
    return int(start_str), int(stop_str)
