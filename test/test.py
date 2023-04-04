import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from Services.contentScraping import *

#get_cat_news(trial_collection,APPS)

#get_article_details(trial_collection)

#get_categories(trial_collection)

#get_source_news(source_collection,"The Verge")

#get_successive_articles(trial_collection,10,2)

#init_article('article_id')    

#collection = ARTICLE_COLLECTION
#content_scraping(driver,collection)