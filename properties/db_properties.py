DATABASE_NAME="Newsfeed"
SOURCE_COLLECTION="source"
TRIAL_SOURCE="source_coll"
RSS_FEED_COLLECTION="rssData"
PAGE_COUNT=10

FIELD_MAP = {
    'title': ['title', 'rss_title'],
    'link': ['link', 'url', 'rss_link'],
    'author': ['author', 'creator', 'rss_author'],
    'published': ['published', 'pubDate', 'rss_published'],
    'description': ['description', 'summary', 'content', 'rss_description'],
    'comments':['comment','comments'],    
    'category': ['category', 'tags', 'keywords', 'rss_category']
}


#categories
APPS="apps"
CRYPTO="cryptocurrrentcy"
GAMING="gaming"
INTERNET="internet"
MOBILES="mobiles"
PC="pc/laptops"
LAPTOPS="pc/laptops"
PC_LAPTOPS="pc/latops"
TABLETS="tablets"
PODCASTS="podcasts"
WEARABLES="wearables"
SMART_HOME="smart home"
SOCIAL="social"
SCIENCE="science"
