#!/usr/bin/env python3
"""connect to mongodb"""
from pymongo import MongoClient

if __name__ == "__main__":
    def list_all(mongo_collection):
        """return collection"""    
        client = MongoClient('mongodb://127.0.0.1:27017')
        school_collection = client.my_db.mongo_collection
        schools = school_collection.find()
        return schools
            