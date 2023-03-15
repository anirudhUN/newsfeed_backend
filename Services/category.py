import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def category_bar(user_cat):
    categories = get_categories(article_collection)
    if user_cat in categories:
        cat_news = get_cat_news(article_collection,user_cat)
    else:
        cat_news = []  
    return {"category": user_cat, "articles": cat_news}