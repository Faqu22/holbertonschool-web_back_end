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
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
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
                f_split[len(f_split) - 1] = f_split[len(f_split) - 1].strip(
                    "\n")
                subcontent.append(f_split)
        return subcontent
