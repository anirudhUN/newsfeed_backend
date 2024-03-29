import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def retrieve_articles_for_category(user_cat, page=None):
    if page is None:
        page = 1
    categories = get_categories(article_collection)
    if user_cat in categories:
        articles = get_successive_articles_for_category(article_collection,user_cat,page)
    else:
        articles = []
    return {"Category": user_cat, "articles": articles}

def generate_category_list(article_collection):
    categories = get_categories(article_collection)
    return {'categories':categories}