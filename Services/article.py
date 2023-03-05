import pymongo
from pymongo import MongoClient
from db_properties import *
from mongo_utils import *
import time

def fetch_article():
    articles = source_collection.find({}).sort('LastAccessTime', pymongo.DESCENDING)
    return articles

while True:
    articles = fetch_article()
    if articles:
        print(articles['content'])
    else:
        time.sleep(1200)  


def get_tag_news(tag):
      results=source_collection.find({"Tags":tag},{})
      for i in results:
            print(i)
