import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

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