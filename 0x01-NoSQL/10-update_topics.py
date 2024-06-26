#!/usr/bin/env python3
'''this module contains a  Python function that lists all documents in a collection'''
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    ''' changes all topics of a school document based on the name'''
    mongo_collection.update_many({"name" : name}, {'$set': {"topics" : topics}})
