#!/usr/bin/env python3
""" 8-main """

def schools_by_topic(mongo_collection, topic):
    """
        create Document with kwargs in db
    """

    return mongo_collection.find({"topics": topic})