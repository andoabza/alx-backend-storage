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
        to_byte = bytes(str(uuid.uuid1()), 'utf-8')
        new_data = bytes(data)
        self._redis.set(new_data, to_byte)
        return self._redis.get(new_data)