from pymongo import MongoClient
from passwords import pswd
import pandas as pd
import json
import os


def mongoimport_json(json_path, db_name, collection_name, client):
    """ Imports a json file at path json_path to a mongo colection
       returns: count of the documants in the new collection
       """
    with open(json_path, encoding='utf8') as f:
        db = client[db_name]
        coll = db[collection_name]
        payload = json.load(f)
        coll.drop()
        coll.insert_many(payload)
    return coll.estimated_document_count()


json_path = os.path.abspath('json')
db_name = 'test'
collection_name = 'apt2'
cluster = f"mongodb+srv://itaysegev11:{pswd}@cluster0.07hxrbu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)


print(mongoimport_json(json_path, db_name, collection_name, client))

print(client.list_database_names())
