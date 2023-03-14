import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from related_articles import *

def init_article(article_id):
    article = get_article_details(article_id)
    related_articles = get_related_articles(article_id)

    return related_articles, article
   



