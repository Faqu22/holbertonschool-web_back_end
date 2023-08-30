#!/usr/bin/env python3
"""
Task 1
"""
import asyncio
import random
from typing import List

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Asynchronous coroutine that waits for a random delay."""
    wait_random = __import__('0-basic_async_syntax').wait_random
    delays = []
    while(n):
        delays.append(wait_random(max_delay))
    return delays
