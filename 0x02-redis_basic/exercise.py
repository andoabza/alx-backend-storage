#!/usr/bin/env python3
"""redis basic"""
import redis
import uuid


class Cache:
    '''a class that will insert data'''
    def __init__(self):
        '''initialization'''
        self._redis = redis.Redis(host='localhost')
        self._redis.flushdb()

    def store(self, data):
        result = self._redis.set(data, uuid.uuid1())
        return result.get(data)