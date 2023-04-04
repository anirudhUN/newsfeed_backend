import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def init_home_page(article_collection,page=None):
    if page is None:
        page = 1
    categories = get_categories(article_collection)
    articles = get_successive_articles(article_collection,page)
    return {'categories': categories, 'articles': articles}