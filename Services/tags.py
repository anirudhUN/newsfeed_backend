import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

def retrive_articles_for_tag(tag,page):
    if page is None:
        page = 1
    articles=get_tag_news(article_collection,tag,page)
    return {'articles':articles}
