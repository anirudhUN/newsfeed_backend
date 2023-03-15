import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
import time
import threading


def insert_rss_doc(collection, url):
    latest_article = collection.find_one(sort=[("published", pymongo.DESCENDING)])
    feed = feedparser.parse(url)
    for item in feed.entries:
        doc = {}
        for field, names in FIELD_MAP.items():
            for name in names:
                if name in item:
                    if field == 'published':
                        date_str = item[name]
                        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
                        date_obj = date_obj.replace(tzinfo=None)
                        doc[field] = date_obj
                    else:
                        doc[field] = item[name]
                    break
        
        if latest_article is None or doc['published'] > latest_article['published'].replace(tzinfo=None):
            insert_one(collection,doc)

def process_rss_feeds():
    for doc in rssfeed_collection.find():
        rss_url = doc['RSSFeedURL']
        insert_rss_doc(article_collection, rss_url)
    time.sleep(20 * 60)
    process_rss_feeds()
