#!/usr/bin/env python3
'''this module contains a  Python function
that lists all documents in a collection'''


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    stat = collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{collection.count_documents({})} logs')
    print("Methods:")
    print(f'method GET: {get}')
    print(f'method POST: {post}')
    print(f'method PUT: {put}')
    print(f'method PATCH: {patch}')
    print(f'method DELETE: {delete}')
    print(f'{stat} status check')
