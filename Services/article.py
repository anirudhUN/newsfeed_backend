
def init_article():
    articles = list(get_article_details())
    tag = list(get_tag_news())
    relative_links = list(get_relative_links(article[_id]))
    return({'tag' : tag, 'articles':articles,'relative_links': relative_links})
