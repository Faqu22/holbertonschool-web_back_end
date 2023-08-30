#!/usr/bin/env python3
"""
Task 6 - sum mixed list function
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function sum_mixed_list
    """
    x = 0.0
    for i in mxd_lst:
        x = i + x
    return x
