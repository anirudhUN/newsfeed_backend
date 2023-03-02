import pymongo
from pymongo import MongoClient
from db_properties import *


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


def get_article_details():
    
   
    articles = source_collection.find().sort('Timestamp', -1).limit(10)
    
    article_details = []
    for article in articles:
        details = {
            'title': article['Title'],
            'summary': article['Summary'],
            'image_url': article['CoverImgURL'],
            'timestamp': article['Timestamp'],
            'source': article['Source'],
            'tags': article['Tags']
        }
        article_details.append(details)
   
    for articles in article_details:
         print(article)

def delete_documents():
      results = source_collection.delete_many()
      return results

def delete_document():
    result = source_collection.delete_one()
    return result

def update_documents():
    results = source_collection.update_many()
    for i in results:
        print(i)

def update_document():
    result = source_collection.update_one()
    return result