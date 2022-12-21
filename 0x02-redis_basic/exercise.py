#!/usr/bin/env python3
"""
Practice with redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count calls function decorate
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for decorator functionality
        """
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call history function decorate
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for decorator functionality
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output
    return wrapper


def replay(fn: Callable):
    """
    Display the history of calls of a particular function
    """
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')
    inside = r.lrange(f_name + ":inputs", 0, -1)
    outside = r.lrange(f_name + ":outputs", 0, -1)
    for key, value in zip(inside, outside):
        try:
            key = key.decode('utf-8')
        except Exception:
            key = ""
        try:
            value = value.decode('utf-8')
        except Exception:
            value = ""
        print(f'{f_name}(*{key}) -> {value}')


class Cache:
    """
    Class Cache
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        # key = self.redis.get("key")
        # if key is None:
        #     key = self.redis.set("key", data)
        return rand_key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Get data from redis
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        get str method
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        get int method
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
