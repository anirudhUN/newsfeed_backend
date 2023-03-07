import sys
sys.path.insert(0, '/path/to/other/folder') # path from newsfeed_backend to services folder, path can change so not specified. 

from db_properties import *
from mongo_utils import *

def init_home_page():
    categories = get_categories()
    articles = list(get_article_details())
    return({'categories':categories, 'articles':articles,'page':0})

def update_home_page(last_page_count):
    page_to_fetch = last_page_count + 1
    articles = get_successive_articles(SOURCE_COLLECTION,PAGE_COUNT,page_to_fetch)
    return list(articles)
