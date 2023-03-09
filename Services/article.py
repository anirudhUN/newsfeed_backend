from properties.db_properties import *
from utils.mongo_utils import *

def init_article():
    article_id = 'article_id'
    article = get_article_details(article_id)
    tags = article['tags']

    related_articles = set()
    for tag in tags:
        related_articles = source_collection.find({'tags': tag})
        for related_article in related_articles:
            if related_article['_id'] != article['_id'] and related_article not in related_articles:
                related_articles.add(related_article)

    return related_articles,article
    
   



