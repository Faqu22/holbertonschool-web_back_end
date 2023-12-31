#!/usr/bin/env python3
""" 8-main """


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Index range
    """
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page
        """
        assert isinstance(page_size, int)
        assert isinstance(page, int)
        assert page > 0
        assert page_size > 0
        subcontent = []
        index = index_range(page, page_size)
        with open("Popular_Baby_Names.csv", "r") as file:
            f_read = file.readlines()
            if len(f_read) < page * page_size:
                return []
            for i in range(index[0] + 1, index[1] + 1):
                f_split = f_read[i].split(",")
                x = f_split[len(f_split) - 1].strip("\n")
                f_split[len(f_split) - 1] = x
                subcontent.append(f_split)
        return subcontent

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get hyper
        """
        hyper = {}
        with open("Popular_Baby_Names.csv", "r") as file:
            f_read = file.readlines()
            hyper["page_size"] = page_size
            hyper["page"] = page
            hyper["data"] = self.get_page(page, page_size)
            if not hyper["data"]:
                hyper["page_size"] = 0
            hyper["total_pages"] = int(len(f_read) / page_size)
            if page == hyper["total_pages"]:
                hyper["next_page"] = None
            else:
                hyper["next_page"] = page + 1
            hyper["prev_page"] = None if page < 2 else page - 1

        return hyper
