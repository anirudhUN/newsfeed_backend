import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from services.home import *
from services.category import *
from services.article import *
from bson import ObjectId
from flask import Flask,Blueprint, jsonify

bp = Blueprint('api', __name__)


@bp.route('/home')
def get_home_data():
    home_data = init_home_page(article_collection,page=None)
    articles = home_data['articles']
    for article in articles:
        article['_id'] = str(article['_id'])  
    return jsonify({
        'categories': home_data['categories'],
        'articles': articles
    })

@bp.route('/category')
def get_category():
    categories = category_collection.find()
    category_list = [category['Category'] for category in categories]
    return jsonify({'Categories': category_list})

@bp.route('/category/<user_cat>/article')
def get_category_article_data(user_cat):
    category_data = retrieve_articles_for_category(user_cat,page=None)
    articles = category_data['articles']
    for article in articles:
        article['_id'] = str(article['_id'])  
    return jsonify({'category': user_cat, 'articles' : articles})

@bp.route('/article/<string:article_id>')
def get_article_data(article_id):
    article_data = init_article(article_id)
    return jsonify({
        'Article': article_data['article'],
        'Related_articles' : article_data['related_articles']
    })