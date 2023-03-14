import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def init_home_page(last_page_count):
    categories = get_categories(source_collection)
    articles = list(get_successive_articles(source_collection,PAGE_COUNT,last_page_count))
    return {'categories':categories, 'articles':articles,'page':last_page_count}

def update_home_page(last_page_count):
    page_to_fetch = last_page_count + 1
    articles = get_successive_articles(source_collection,PAGE_COUNT,page_to_fetch)
    return list(articles)

def category_bar(user_cat):
    categories = get_categories(source_collection)
    if user_cat in categories:
        cat_news = get_cat_news(source_collection,user_cat)
    else:
        cat_news = []
    return {"category": user_cat, "articles": cat_news}

