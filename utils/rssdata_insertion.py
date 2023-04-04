import sys
import os
import pandas as pd
from datetime import datetime

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

rssfeed_collection.delete_many({})
category_collection.delete_many({})

df=pd.read_csv("git_re\\newsfeed_backend\\data\\RSSfeed_details.csv")
data=df.to_dict(orient="records")
rssfeed_collection.insert_many(data)
current_time = datetime.now()
for document in rssfeed_collection.find():
    current_time = datetime.now()
    rssfeed_collection.update_one({'_id': document['_id']}, {'$set': {'last_access_time': current_time}})
rssfeed_collection.update_many({}, {'$set': {'Status': "True"}})
categories = df['Category'].tolist()

for category in categories:
    category_doc = {'Category': category}
    category_collection.insert_one(category_doc)