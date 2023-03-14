import pymongo
import pandas as pd
import json
import datetime
from pymongo import MongoClient

client = MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")
db = client['Newsfeed']
collection = db['rssData']

#collection.delete_many({})

df=pd.read_csv("C:\\Users\\Dhanush Gowda\\Downloads\\Data Model and Functional Requirements - RSSfeed.csv")
data=df.to_dict(orient="records")
#collection.insert_many(data)

current_time = datetime.datetime.now()
for document in collection.find():
    current_time = datetime.datetime.now()
    collection.update_one({'_id': document['_id']}, {'$set': {'last_access_time': current_time}})
    
collection.update_many({}, {'$set': {'Status': "True"}})

print(f"{collection.count_documents({})} documents updated.")