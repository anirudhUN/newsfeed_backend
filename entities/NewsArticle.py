class NewsArticle:
    def __init__(self,source,title,summary,article_content,author_name,timestamp,article_url,cover_img_url,tags,comments,category):
        self.source=source
        self.title=title
        self.summary=summary
        self.article_content=article_content
        self.author_name = author_name
        self.timestamp = timestamp
        self.article_url=article_url
        self.category = category
        self.cover_img_url = cover_img_url
        self.tags = tags
        self.comments=comments
