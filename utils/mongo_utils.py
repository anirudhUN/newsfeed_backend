import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import pymongo
from pymongo import MongoClient
from properties.db_properties import *
from bson import ObjectId
import feedparser
from datetime import datetime

cluster=MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")

database=cluster[DATABASE_NAME]
rssfeed_collection=database[RSS_FEED_COLLECTION]
article_collection=database[ARTICLE_COLLECTION]
category_collection=database[CATEGORY_COLLECTION]




def insert_one(collection,document):
    collection.insert_one(document)
    

def insert_many(collection,documents):
    collection.insert_many(documents)
    

def get_categories(collection_name):
    categories=collection_name.distinct('category')
    return list(categories)

def get_cat_news(collection_name,category):
        results=collection_name.find({"category":category},{})
        return list(results)


def get_tag_news(collection_name,tag):
      results=collection_name.find({"Tags":tag},{})
      return list(results)


def get_source_news(collection_name,source):
      results=collection_name.find({"Source":source},{})
      return list(results)


def get_sources(collection_name):
      results=collection_name.distinct("Source")
      return list(results)


def get_successive_articles(collection,page):
    skip_count = (page - 1) * ARTICLE_COUNT
    cursor = collection.find({},{"title":1,"published":1,"description":1,"category":1}).sort("published", -1).skip(skip_count).limit(ARTICLE_COUNT)
    return list(cursor)

def get_successive_articles_for_category(collection, category, page):
    skip_count = (page - 1) * ARTICLE_COUNT
    cursor = collection.find({"category": category},{"title":1, "published":1, "description":1, "category":1}).sort("published", -1).skip(skip_count).limit(ARTICLE_COUNT)
    return list(cursor)

def delete_documents(collection_name,query):
    collection_name.delete_many(query)

def delete_document(collection_name,query):
    collection_name.delete_one(query)
    

def update_documents(collection_name,query,update):
    collection_name.update_many(query,update)

def update_document(collection_name,query,update):
    collection_name.update_one(query,update)
    
    
def get_article_details(collection,article_id):
    article = collection.find_one({'_id': ObjectId(article_id)})
    if article is None:
        print(f"No article found with ID {article_id}")
        return None
    else:
        return article
    
def related_links(collection_name,article_id):
    category = collection_name.find({"_id":article_id},{"category":1})
    links=collection_name.find({"category":category},{"title":1,"link":1})
    return list(links)


def get_latest_articles(collection):
    cursor = collection.find({},{"title":1,"published":1,"description":1,"category":1}).sort("published", -1).limit(ARTICLE_COUNT)
    return list(cursor)


