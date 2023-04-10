import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from services.related_articles import *

def init_article(article_id):
    article = get_article_details(article_id)
    related_articles = get_related_articles(article_id)

    # Convert ObjectId objects to strings
    if article.get('_id'):
        article['_id'] = str(article['_id'])
    for related_article in related_articles:
        if related_article.get('_id'):
            related_article['_id'] = str(related_article['_id'])

    return {'article': article, 'related_articles': related_articles}





