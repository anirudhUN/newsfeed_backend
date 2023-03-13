import pymongo
from pymongo import MongoClient
from properties.db_properties import *
from bson import ObjectId
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
    
def get_article_details(article_id):
    article = source_collection.find_one({'_id': ObjectId(article_id)})
    if article is None:
        print(f"No article found with ID {article_id}")
        return None
    else:
        return article
    
def related_links(collection_name,article_id):
    category = collection_name.find({"_id":article_id},{"category":1})
    links=collection_name.find({"category":category},{"title":1,"link":1})
    return list(links)

def get_related_articles(article_id):
    article = get_article_details(article_id)
    tags = article['tags']
    category = article['category']
    related_articles = []

    for tag in tags:
        tag_related_articles = source_collection.find({'tags': tag, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        for related_article in tag_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)
                break

    for cat in category:
        cat_related_articles = source_collection.find({'category': cat, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        for related_article in cat_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)
                break

    return related_articles


