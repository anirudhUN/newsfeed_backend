import sys
sys.path.insert(0, '/path/to/other/folder') # path from newsfeed_backend to services folder, path can change so not specified. 

from db_properties import *
from mongo_utils import *

def init_article():
    articles = list(get_article_details())
    tag = list(get_tag_news())
    relative_links = list(get_relative_links(article[_id]))
    return({'tag' : tag, 'articles':articles,'relative_links': relative_links})
