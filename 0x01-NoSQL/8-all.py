#!/usr/bin/env python3
"""connect to mongodb"""


if __name__ == "__main__":
    def list_all(mongo_collection):
        """return collection"""
        return mongo_collection.find()
