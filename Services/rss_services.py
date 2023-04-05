import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
import time
import threading


def insert_rss_doc(collection, url,last_access_time,source_name):
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
                    doc['Source']=source_name
                    break
        if last_access_time is None or doc['published'] > last_access_time.replace(tzinfo=None):
            collection.insert_one(doc)
            for category, urls in CATEGORY_MAP.items():
                if url in urls:
                    article_collection.update_one({'_id': doc['_id']}, {'$set': {'Category': category}})
                    break

def process_rss_feeds():
    for doc in rssfeed_collection.find():
        rss_url = doc['RSSFeedURL']
        last_access_time = doc['last_access_time']
        source_name=doc['Name']
        insert_rss_doc(article_collection, rss_url,last_access_time,source_name)
        current_time = datetime.now()
        rssfeed_collection.update_one({'_id': doc['_id']}, {'$set': {'last_access_time': current_time}})
    time.sleep(20 * 60)
    process_rss_feeds()

if __name__=="__main__":
    process_rss_feeds()