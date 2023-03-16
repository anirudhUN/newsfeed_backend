DATABASE_NAME="Newsfeed"
ARTICLE_COLLECTION="articleData"
RSS_FEED_COLLECTION="rssData"
ARTICLE_COUNT=10
TRIAL_COLLECTION = "source_coll"
FIELD_MAP = {
    'title': ['title', 'rss_title'],
    'link': ['link', 'url', 'rss_link'],
    'author': ['author', 'creator', 'rss_author'],
    'published': ['published', 'pubDate', 'rss_published'],
    'description': ['description', 'summary', 'content', 'rss_description'],
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
