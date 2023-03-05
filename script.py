import pymongo
import pandas as pd
import json
import datetime
from mongo_utils import *

df=pd.read_csv("Data Model and Functional Requirements - Sheet5.csv")
data=df.to_dict(orient="records")
#collection.insert_many(data)
def update_rss(collection):
    collection.insert_many(data)
    current_time = datetime.datetime.now()
    for document in collection.find():
        current_time = datetime.datetime.now()
        collection.update_one({'_id': document['_id']}, {'$set': {'last_access_time': current_time}})
        
    collection.update_many({}, {'$set': {'Status': "True"}})
    
    print(f"{collection.count_documents({})} documents updated.")

update_rss(rssfeed_collection)