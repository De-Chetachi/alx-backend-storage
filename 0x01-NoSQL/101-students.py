#!/usr/bin/env python3
'''this module contains a  Python function
that lists all documents in a collection'''


def top_students(mongo_collection):
    '''returns all students sorted by average score:'''
    docs = mongo_collection.find({})
    for doc in docs:
        topics = doc["topics"]
        score = 0
        for topic in topics:
            score += topic["score"]
        avg = score / len(topics)
        mongo_collection.update_one(doc, {'$set': {"averageScore": avg}})
        # doc["averageScore"] =  avg
    new_docs = mongo_collection.find({})
    return sorted(new_docs, reverse=True, key=lambda doc:
                  doc.get("averageScore"))
