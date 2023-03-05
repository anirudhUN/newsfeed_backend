from db_properties import *
from mongo_utils import *

def get_article():
    article_details = get_article_details()
    articles = []
    for article in article_details:
        articles.append(article)
    return articles
 
def get_tag():
    tag=get_tag_news()
    return tag
   
