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


#to insert directly using rss feed url
def insert_rss_doc(collection,url, FIELD_MAP):
    feed = feedparser.parse(url)
    for item in feed.entries:
        doc = {}
        for field, names in FIELD_MAP.items():
            for name in names:
                if name in item:
                    if field == 'published':
                        date_obj = datetime.strptime(item[name], '%a, %d %b %Y %H:%M:%S %z')
                        doc[field] = date_obj
                    else:
                        doc[field] = item[name]
                    break
        collection.insert_one(doc)


def insert_one(collection,document):
    result = collection.insert_one(document)
    return result

def insert_many(collection,documents):
    result = collection.insert_many(documents)
    return result

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


def get_successive_articles(collection,n, page):
    skip_count = (page - 1) * n
    cursor = collection.find({},{"title":1,"published":1,"description":1,"category":1}).skip(skip_count).limit(n)
    return list(cursor)

def delete_documents(collection_name,query):
    collection_name.delete_many(query)

def delete_document(collection_name,query):
    result = collection_name.delete_one(query)
    return result

def update_documents(collection_name,query,update):
    results = collection_name.update_many(query,update)

def update_document(collection_name,query,update):
    result = collection_name.update_one(query,update)
    return result
    
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

def get_related_articles(collection,article_id):
    article = get_article_details(article_id)
    tags = article['tags']
    category = article['category']
    related_articles = []

    for tag in tags:
        tag_related_articles = collection.find({'tags': tag, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        for related_article in tag_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)
                break

    for cat in category:
        cat_related_articles = collection.find({'category': cat, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        for related_article in cat_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)
                break

    return related_articles


if __name__=="__main__":
    insert_rss_doc(article_collection,"https://mobilesyrup.com/feed/",FIELD_MAP)