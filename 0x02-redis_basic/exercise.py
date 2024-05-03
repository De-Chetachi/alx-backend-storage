#!/usr/bin/env python3
'''a class module'''
import redis
from uuid import uuid4
from typing import Union


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
        
