import sys
sys.path.append('C:\Users\aniru\Desktop\newsfeed')
from db_properties import *
from mongo_utils import *

get_article_details()
get_tag_news()
get_successive_articles()
