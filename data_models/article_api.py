import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from Services.article import *
from bson import ObjectId
from flask import Flask, jsonify

app = Flask(__name__)

class ARTICLE():
    def __init__(self):
        self.title = ''
        self.description = ''
        self.article_content = ''
        self.image_url = ''
        self.author = ''
        self.category = ''
        self.published = ''
        self.tags = ''
        self.Source = ''

@app.route('/article/<string:article_id>')
def get_article_data(article_id):
    article_data = init_article(article_id)
    article = article_data['article']

    article_obj = ARTICLE()
    article_obj.title = str(article['title'])
    article_obj.description = str(article['description'])
    article_obj.image_url = str(article.get('image-url', ''))
    article_obj.author = str(article['author'])
    article_obj.category = str(article['category'])
    article_obj.published = str(article.get('published', ''))
    article_obj.article_content = str(article.get('article-content', ''))
    article_obj.tags = str(article.get('tags', ''))
    article_obj.Source = str(article.get('Source', ''))
    
    return jsonify({
        'Article': article_obj.__dict__,
        'Related_articles' : article_data['related_articles']
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)
