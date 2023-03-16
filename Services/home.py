import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def init_home_page(article_collection):
    categories = get_categories(article_collection)
    articles = list(get_latest_articles(article_collection))
    return {'categories':categories, 'articles':articles}

def update_home_page(article_collection,page):
    articles = get_successive_articles(article_collection, page)
    return list(articles)