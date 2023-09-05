    #!/usr/bin/env python3
""" 8-main """

def update_topics(mongo_collection, name, topics):
    """
        create Document with kwargs in db
    """

    myquery = {"name": name}
    newquery = {"$set": {"topics": topics}}
    mongo_collection.update_many(myquery, newquery)
