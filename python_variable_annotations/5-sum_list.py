#!/usr/bin/env python3
"""
Task 5 - sum list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function sum_list
    """
    x = 0.0
    for i in input_list:
        x = i + x
    return x
