#!/usr/bin/env python3
""" 8-main """

def insert_school(mongo_collection, **kwargs):
    """
        create Document with kwargs in db
    """
    
    return mongo_collection.insert_one(kwargs).inserted_id