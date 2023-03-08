from db_properties import *
from mongo_utils import *

def init_tile():
    categories = get_categories()
    articles = list(get_article_details())
    tag = list(get_tag_news())
    relative_links = list(get_relative_links(article[_id]))
    return({'categories':categories, 'articles':articles, 'tag' : tag, 'relative_links': relative_links})
