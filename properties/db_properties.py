DATABASE_NAME="Newsfeed"
ARTICLE_COLLECTION="articleData"
RSS_FEED_COLLECTION="rssData"
ARTICLE_COUNT=10
COMMENT_COUNT = 3
TRIAL_COLLECTION = "source_coll"
FIELD_MAP = {
    'title': ['title', 'rss_title'],
    'link': ['link', 'url', 'rss_link'],
    'author': ['author', 'creator', 'rss_author'],
    'published': ['published', 'pubDate', 'rss_published'],
    'description': ['description', 'summary', 'content', 'rss_description'],
    'category': ['category', 'tags', 'keywords', 'rss_category']
}

PATH = "..\chromedriver.exe"

SOURCE_SELECTOR_MAPPER={
             "Techcrunch" : "div.article-content",
             "Tech republic": "section.article-body",
             "Tech Talksick":"div.text",
             "Firstpost Tech":"div.text-content-wrap",
             "Hackaday":"div.entry-content",
             "MobileSyrup": "div.article-content",
             "Droid Life":"div.entry-content__post",
             "Droidviews":"div.entry-content"
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
