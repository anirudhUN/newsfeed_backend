from properties.db_properties import *
from utils.mongo_utils import *

def init_article():
    article_id = 'article_id'
    article = get_article_details(article_id)
    related_articles = get_related_articles(article_id)

    return related_articles, article


    
   



