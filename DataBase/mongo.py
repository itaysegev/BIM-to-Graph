from pymongo import MongoClient
from passwords import pswd
import pandas as pd
import json
import os


def mongoimport(csv_path, db_name, collection_name, client):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    db = client[db_name]
    coll = db[collection_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return coll.count()


csv_path = os.path.abspath('apt2.csv')
db_name = 'test'
collection_name = 'apt2'
cluster = f"mongodb+srv://itaysegev11:{pswd}@cluster0.07hxrbu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)
mongoimport(csv_path, db_name, collection_name, client)

print(client.list_database_names())
