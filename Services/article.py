from properties.db_properties import *
from utils.mongo_utils import *

def init_article():
    article_id = 'article_id'
    article = get_article_details(article_id)
    tags = article['tags']
    category = article['category']

    related_articles = []
    for tag in tags:
        related_article = source_collection.find_one({'tags': tag, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        if related_article:
            related_articles.append(related_article)

    for cat in category:
        related_article = source_collection.find_one({'category': cat, '_id': {'$ne': article['_id']}}, projection={'_id': 0, 'title': 1, 'description': 1})
        if related_article:
            related_articles.append(related_article)

    return related_articles, article
    
   



