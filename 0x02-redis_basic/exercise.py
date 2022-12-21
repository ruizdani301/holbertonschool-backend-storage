#!/usr/bin/env python3
"""0. Writing strings to Redis"""
from uuid import uuid4
from typing import Union, Callable
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Task 2
    count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function that increments the key"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """ Task 0
    class Cache
    """
    
    def __init__(self):
        """ Task 0
        method constructor"""

        self._redis = redis.Redis()
        self._redis.flushdb()


    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Task 0
        method store"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """task 1"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Task 1"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Task 1"""
        try:
            val = int(self._redis.get(key))
        except ValueError:
            val = 0
        return val
