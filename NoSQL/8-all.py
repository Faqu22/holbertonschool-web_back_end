#!/usr/bin/env python3
""" 8-main """

def list_all(mongo_collection):
    """
        List all in db
    """
    return [i for i in mongo_collection.find()]