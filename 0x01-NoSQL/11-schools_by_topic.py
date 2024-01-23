#!/usr/bin/env python3
"""find school by topic"""


def schools_by_topic(mongo_collection, topic):
    """find school by topic"""
    result = mongo_collection.find({'topics': topic})
    return result