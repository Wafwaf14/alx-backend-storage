#!/usr/bin/env python3
"""
Writing strings to redis
"""
import redis
from typing import Any
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """Intantiating our class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """sets a key/value pair in redis and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''From the Redis data storage retrieves a value
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''From the Redis data storage retrieves a string.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''From the Redis data storage retrieves an integer.
        '''
        return self.get(key, lambda x: int(x))
