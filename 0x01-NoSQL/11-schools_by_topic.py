#!/usr/bin/env python3
'''this module contains a  Python function that lists all documents in a collection'''
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    ''' returns the list of school having a specific topic:'''
    list_ = []
    schools = mongo_collection.find()
    for school in schools:
        if topic in school["topics"]
            list_.append(school)
    return list_
