from db_properties import *
from mongo_utils import *

def init_article():
    article = get_article_details(SOURCE_COLLECTION, limit=1)[0]
    
    tags = article['tags']
    url = article['url']
  
    for tag in tags:
        related_link = f'<a href="{url}?tag={tag}">{tag}</a>'
        return(related_link)
    
    for article in article.values():
        return(article)
    
   



