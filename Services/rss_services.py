import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
import time
import threading

def process_rss_feeds():
    for doc in rssfeed_collection.find():
        rss_url = doc['RSSFeedURL']
        insert_rss_doc(article_collection, rss_url)

if __name__=="__main__":
    while True:
        process_rss_feeds()
        time.sleep(20 * 60)