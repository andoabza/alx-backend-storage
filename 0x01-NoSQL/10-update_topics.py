#!/usr/bin/env python3
"""update a document in a collection based on kwargs"""


def update_topics(mongo_collection, name, topics):
    myquery = { "name": name }
    newvalues = { "$set": { 'topics': topics } }
    return mongo_collection.update_one(myquery, newvalues)