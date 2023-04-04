import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from services import *

def get_related_articles(article_id):
    article = get_article_details(article_id)
    tags = article['tags']
    category = article['category']
    related_articles = []

    for tag in tags:
        tag_name = tag['name']
        tag_related_articles = article_collection.find({'tags.name': tag_name, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        for related_article in tag_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)
        
    if isinstance(category, str):
        cat_related_articles = article_collection.find({'category': category, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        for related_article in cat_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)

    return related_articles