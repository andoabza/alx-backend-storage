#!/usr/bin/env python3
"""insert data"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id