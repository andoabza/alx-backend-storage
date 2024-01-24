#!/usr/bin/env python3
'''insert data to store in redis'''
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    '''class to store data in redis'''
    def __init__(self):
        '''constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store data in redis'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str) -> Union[str, bytes, int, float]:
        '''get data from redis'''
        return data

    