DATABASE_NAME="Newsfeed"
ARTICLE_COLLECTION="articleData"
RSS_FEED_COLLECTION="rssData"
CATEGORY_COLLECTION="categoryData"
ARTICLE_COUNT=10
COMMENT_COUNT = 3
TRIAL_COLLECTION = "source_coll"
FIELD_MAP = {
    'title': ['title', 'rss_title'],
    'link': ['link', 'url', 'rss_link'],
    'author': ['author', 'creator', 'rss_author'],
    'published': ['published', 'pubDate', 'rss_published'],
    'description': ['description', 'summary', 'content', 'rss_description']
}
CATEGORY_MAP = {
    'Laptops/mobiles': [
        'https://techcrunch.com/mobile/feed/',
        'https://www.techrepublic.com/rssfeeds/topic/android/',
        'https://www.techrepublic.com/rssfeeds/topic/mobile/',
        'https://www.droidviews.com/feed/',
        'https://www.droid-life.com/feed/',
        'https://mobilesyrup.com/feed/'
    ],
    'Startup': [
        'https://techcrunch.com/startups/feed/',
        'https://www.techrepublic.com/rssfeeds/topic/start-ups/'
    ],
    'Technology': [
        'https://www.techrepublic.com/rssfeeds/topic/artificial-intelligence/',
        'https://www.techrepublic.com/rssfeeds/topic/cloud/',
        'https://techtalksick.com/feed/',
        'https://www.firstpost.com/tech/feed',
        'https://hackaday.com/blog/feed/',
        'https://www.techrepublic.com/rssfeeds/topic/internet/',
        'https://www.techrepublic.com/rssfeeds/topic/digital-media/',
        'https://www.techrepublic.com/rssfeeds/topic/innovation/',
        'https://www.techrepublic.com/rssfeeds/topic/internet-of-things/',
        'https://www.techrepublic.com/rssfeeds/topic/tech-and-work/'
    ]
}

PATH = "..\chromedriver.exe"

SOURCE_SELECTOR_MAPPER={
"Tech republic": {
   'article': "section.article-body",
   'tags' : 'section.categories ul li a',
   'image' : 'section.article-body figure img'
},
 "Techcrunch": {
    'article': 'div.article-content',
    'tags': 'div.article__tags h3 + ul li a',
    'image' : 'div.article__content-wrap img'
},
"Tech Talksick" :{
    'article': 'div.text',
    'tags': 'div.bottom-tags p a',
    'image' : 'div.epcl-loader img'
},
"Firstpost Tech": {
    "article" : "div.text-content-wrap",
    'tags' : "div.article__tags ul li a",
    'image' : 'figure.wp-caption img'
},
"Hackaday":{
    'article' : "div.entry-content",
    'tags' : "span.tags-links a",
    'image' : "div.entry-featured-image img"
},
"MobileSyrup": {
    'article' : "div.article-content",
    'tags' : "",
    'image' : "div.main.has-sidebar img"
},
"Droid Life": {
    'article' : "h1.entry-title",
    'tags' : "div.entry-taxonomy entry-taxonomies__category ul li a",
    'image' : "div.picture.picture__post-featured img"
},
"Droidviews": {
    'article' : "h1.entry-title",
    'tags' : "",
    'image' : "div.entry-content p img"
}
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
