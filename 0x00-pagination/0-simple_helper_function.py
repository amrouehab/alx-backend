#!/usr/bin/env python3
"""
This module provides a helper function to calculate index range for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start and end index for the given pagination params.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end

