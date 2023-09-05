#!/usr/bin/env python3
""" 8-main """


def index_range(page, page_size):
    """
    Index range
    """
    return ((page - 1) * page_size, page_size * page)
