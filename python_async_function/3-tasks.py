#!/usr/bin/env python3
"""
Task 2
"""

from typing import List
import asyncio
import time
from asyncio import Task


def task_wait_random(max_delay: int) -> Task:
    """Asynchronous coroutine that waits for a random delay."""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
