import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from services import *

def get_related_articles(article_id):
    article = get_article_details(article_id)
    tags = article['Tags']
    category = article['Category']
    related_articles = []

      # Get related articles based on tags
    for tag in tags:
        tag_name = tag['name']
        tag_related_articles = article_collection.find({'Tags.name': tag_name, '_id': {'$ne': article['_id']}}, projection={"title":1, "published":1, "description":1, "Category":1, 'ImageURL':1, 'author':1})
        for related_article in tag_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)

    if not related_articles:
        cat_related_articles = article_collection.find({'Category': category, '_id': {'$ne': article['_id']}}, projection={"title":1, "published":1, "description":1, "Category":1, 'ImageURL':1, 'author':1})
        for related_article in cat_related_articles:
            if related_article not in related_articles:
                related_articles.append(related_article)
    related_articles = related_articles[:3]

    return related_articles