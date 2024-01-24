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

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        '''get data from redis'''
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        '''get data from redis as string'''
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        '''get data from redis as int'''
        return self.get(key, int)
    
    @property
    def count_calls(self: Callable) -> Callable:
        '''count calls'''
        return self._redis.count(self)
