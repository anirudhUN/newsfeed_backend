import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def init_home_page(article_collection,PAGE_COUNT):
    categories = get_categories(article_collection)
    articles = list(get_latest_articles(article_collection,PAGE_COUNT))
    return {'categories':categories, 'articles':articles}

def update_home_page(article_collection,PAGE_COUNT,page):
    articles = get_successive_articles(article_collection,PAGE_COUNT, page)
    return list(articles)