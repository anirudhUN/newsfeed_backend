import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from Services.category import *
from bson import ObjectId
from flask import Flask, jsonify

app = Flask(__name__)

class CATEGORY_ARTICLE():
    def __init__(self):
        self.id = ''
        self.title = ''
        self.description = ''
        self.image_url = ''
        self.category = ''
        self.published = ''

@app.route('/category/<user_cat>/article')
def get_category_data(user_cat):
    category_data = retrieve_articles_for_category(user_cat,page=None)
    articles = category_data['articles']
    data = []
    for article in articles:
        category_article = CATEGORY_ARTICLE()
        category_article.id = str(article['_id'])
        category_article.title = str(article['title'])
        category_article.description = str(article['description'])
        category_article.image_url = str(article.get('image-url', ''))
        category_article.category = str(article['category'])
        category_article.published = str(article.get('published', '')) 
        data.append(category_article.__dict__)
    return jsonify({'category': user_cat, 'articles' : data})

if __name__ == '__main__':
    app.run(debug=True, port=8000)