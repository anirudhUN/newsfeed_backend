import pymongo
from pymongo import MongoClient
from db_properties import *

cluster=MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")

database=cluster[DATABASE_NAME]
source_collection=database[SOURCE_COLLECTION]
rssfeed_collection=database[RSS_FEED_COLLECTION]

def insert_one(document):
    result = source_collection.insert_one(document)
    return result

def insert_many(documents):
    result = source_collection.insert_many(documents)
    return result

def get_categories():
    categories = source_collection.distinct('category')
    for category in categories:
        print(category)


def get_cat_news(category):
        results=source_collection.find({"Category":category},{})
        for i in results:
            print(i)


def get_tag_news(tag):
      results=source_collection.find({"Tags":tag},{})
      for i in results:
            print(i)


def get_source_news(source):
      results=source_collection.find({"Source":source},{})
      for i in results:
            print(i)


def get_sources():
      results=source_collection.distinct("Source")
      for i in results:
            print(i)


def get_article_details(limit, last_access_time): 
    if last_access_time==None:
        articles = source_collection.find({}, {}).limit(limit)
    else:
        articles = source_collection.find({'last_access_time': {'$gt': last_access_time}}).limit(limit)

    article_list = []
    for article in articles:
        article_list.append(article)
    return article_list
    


def delete_documents(query):
      results = source_collection.delete_many(query)
      return results

def delete_document(query):
    result = source_collection.delete_one(query)
    return result

def update_documents(query,update):
    results = source_collection.update_many(query,update)
    for i in results:
        print(i)

def update_document(query,update):
    result = source_collection.update_one(query,update)
    return result

