import sys
sys.path.insert(0, '/path/to/other/folder') # path from newsfeed_backend to services folder, path can change so not specified. 

from db_properties import *
from mongo_utils import *

def get_category():
    category=get_categories()
    return category

def get_article():
    article_details = get_article_details()
    articles = []
    for article in article_details:
        articles.append(article)
    return articles
  
get_relative_links()
