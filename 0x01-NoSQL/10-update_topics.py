#!/usr/bin/env python3
"""update a document in a collection based on kwargs"""

if __name__ == '__main__':
    def update_topics(mongo_collection, name, topics):
        mongo_collection.update({"name": name},{"$set":{"topics": topics}})
