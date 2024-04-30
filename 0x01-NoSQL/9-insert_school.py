#!/usr/bin/env python3
'''this module contains a  Python function that lists all documents in a collection'''
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs'''
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
