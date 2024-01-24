#!/usr/bin/env python3
'''insert data to store in redis'''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''A decorator that counts calls made to the method'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''A decorator that stores the history of inputs and outputs'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(method: Callable):
    '''replay history'''
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode('utf-8')
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    outputs = r.lrange(method_name + ":outputs", 0, -1)
    print("{} was called {} times:".format(method_name, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    '''class to store data in redis'''
    def __init__(self):
        '''constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
