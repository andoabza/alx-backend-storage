#!/usr/bin/env python3
"""update a document in a collection based on kwargs"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update({"name": name},{"$set":{"topics": topics}})
