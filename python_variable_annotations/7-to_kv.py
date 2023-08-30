#!/usr/bin/env python3
"""
Task 7 - TO KV function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function TO_KV
    """
    return (k, (v * v))
