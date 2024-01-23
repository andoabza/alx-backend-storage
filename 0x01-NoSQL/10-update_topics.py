#!/usr/bin/env python3
"""update a document in a collection based on name"""



def update_topics(mongo_collection, name, topics):
    """update a document in a collection based on name""" 
    mongo_collection.update_many(
        {"name": name}, 
        {"$set": {"topics": topics}}
        )