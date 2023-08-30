#!/usr/bin/env python3
"""
Task 8 - Make Multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by the given multiplier
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
