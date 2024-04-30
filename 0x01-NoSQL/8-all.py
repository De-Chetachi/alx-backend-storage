#!/usr/bin/env python3
'''this module contains a  Python function that lists all documents in a collection'''
from pymongo import MongoClient


def list_all(mongo_collection):
    '''lists all documents in a collection'''
    # list_ = []
    # list_.extend(mongo_collection.find())
    # return list_
    return mongo_collection.find()
