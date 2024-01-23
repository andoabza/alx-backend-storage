#!/usr/bin/env python3
"""connect to mongodb"""
from pymongo import MongoClient


if __name__ == "__main__":
    def list_all(mongo_collection):
        """return collection"""    
        school_collection = mongo_collection
        schools = school_collection.find()
        return schools
            