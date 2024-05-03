#!/usr/bin/env python3
'''a class module'''
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    '''cache class'''
    def __init__(self):
        '''initialization for the cache class'''
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''stores data in a random unique generated key'''
        key = str(uuid4())
        self._redis[key] = data
        return key
       

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """takes a key retrieves the value"""
        value = self._redis.get(key)

        if not value:
            return None

        if fn:
            return fn(value)
        return value


    def get_str(value: Union[str, bytes, int, float]) -> str:
        '''converts value to string'''
        return str(value)

    
    def get_int(value: Union[str, bytes, int, float]) -> int:
        '''convrts value to int'''
        return int(value)
