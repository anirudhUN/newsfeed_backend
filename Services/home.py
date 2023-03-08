
def init_home_page():
    categories = get_categories()
    articles = list(get_article_details())
    return({'categories':categories, 'articles':articles,'page':0})

def update_home_page(last_page_count):
    page_to_fetch = last_page_count + 1
    articles = get_successive_articles(SOURCE_COLLECTION,PAGE_COUNT,page_to_fetch)
    return list(articles)

def category_page(user_cat):
    categories = get_categories()
    if user_cat in categories:
         cat_news = get_cat_news(user_cat)
    
    return {"category": user_cat, "articles": cat_news}

