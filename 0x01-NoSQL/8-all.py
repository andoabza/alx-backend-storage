"""!/usr/bin/env python3"""
"""connect to mongodb"""

def list_all(mongo_collection):
    """return collection"""
    return mongo_collection.find()
