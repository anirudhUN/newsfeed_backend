import pymongo
from pymongo import MongoClient
from db_properties import *
import feedparser

cluster=MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")

database=cluster[DATABASE_NAME]
source_collection=database[SOURCE_COLLECTION]
rssfeed_collection=database[RSS_FEED_COLLECTION]
trial_collection=database[TRIAL_SOURCE]


#to insert directly using rss feed url
def insert_rss_doc(url):
    feed=feedparser.parse(url)
    for item in feed.entries:
        author = getattr(item, 'author', None)
        doc = {
            'title': item.title,
            'link': item.link,
            'description': item.description,
            'published': item.published,
            'author':author,
            'category':item.category
        }
        trial_collection.insert_one(doc)



def insert_one(document):
    result = source_collection.insert_one(document)
    return result

def insert_many(documents):
    result = source_collection.insert_many(documents)
    return result

def get_categories(collection_name):
    categories=collection_name.distinct('category')
    for category in categories:
       print(category)

def get_cat_news(collection_name,category):
        results=collection_name.find({"category":category},{})
        for i in results:
            print(i)


def get_tag_news(collection_name,tag):
      results=collection_name.find({"Tags":tag},{})
      for i in results:
            print(i)


def get_source_news(collection_name,source):
      results=collection_name.find({"Source":source},{})
      for i in results:
            print(i)


def get_sources(collection_name):
      results=collection_name.distinct("Source")
      for i in results:
            print(i)


def get_successive_articles(collection,n, page):
    skip_count = (page - 1) * n
    cursor = collection.find().skip(skip_count).limit(n)
    article_list = list(cursor)
    for article in article_list:
        print(article["title"])
        print(article["published"])
        print(article["description"])
        print(article["category"])
        print("")
    


def delete_documents(collection_name,query):
    collection_name.delete_many({query})

def delete_document(collection_name,query):
    result = collection_name.delete_one(query)
    return result

def update_documents(collection_name,query,update):
    results = collection_name.update_many(query,update)
    for i in results:
        print(i)

def update_document(collection_name,query,update):
    result = collection_name.update_one(query,update)
    return result

def get_article_details(collection_name,id): 
    articles = collection_name.find({'_id':id})
    for article in articles:
        print(article["Title"])
        print(article["Summary"])
        print(article["Category"])
        print(article["AuthorNames"])
        print(article["Source"])
        print(article["Comments"])
        print("")
    



