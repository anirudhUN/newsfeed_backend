import pymongo
import pandas as pd
import json
import datetime
from pymongo import MongoClient
from properties.db_properties import *

client = MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")
db = client[DATABASE_NAME]
collection = db[RSS_FEED_COLLECTION]

#collection.delete_many({})

df=pd.read_csv("git_re\\newsfeed_backend\\data\\RSSfeed_details.csv")
data=df.to_dict(orient="records")
#collection.insert_many(data)

current_time = datetime.datetime.now()
for document in collection.find():
    current_time = datetime.datetime.now()
    collection.update_one({'_id': document['_id']}, {'$set': {'last_access_time': current_time}})
    
collection.update_many({}, {'$set': {'Status': "True"}})

print(f"{collection.count_documents({})} documents updated.")