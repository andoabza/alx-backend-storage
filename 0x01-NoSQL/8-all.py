#!/usr/bin/env python3
"""connect to mongodb"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """return collection"""
    client = MongoClient MongoClient("mongodb://localhost:27017/")
    school = client.my_db.mongo_collection
    return school.find()
