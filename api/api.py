import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from services.home import *
from services.category import *
from services.article import *
from services.tags import*
from bson import ObjectId
from flask import Flask,Blueprint, jsonify, request

bp = Blueprint('api', __name__)


@bp.route('/home/<int:page>')
@bp.route('/home', defaults={'page': 1})
def get_home_data(page):
    categories = category_collection.find()
    category_list = [category['Category'] for category in categories]
    home_data = init_home_page(article_collection,page=page)
    articles = home_data['articles']
    for article in articles:
        article['_id'] = str(article['_id'])  
    return jsonify({
       'Categories': category_list,
        'articles': articles
    })

@bp.route('/category')
def get_category():
    categories = category_collection.find()
    category_list = [category['Category'] for category in categories]
    return jsonify({'Categories': category_list})

@bp.route('/category/<category>/<int:page>')
@bp.route('/category/<category>', defaults={'page': 1})
def get_category_article_data(category, page):
    categories = category_collection.find()
    category_list = [category['Category'] for category in categories]
    category_data = retrieve_articles_for_category(category, page=page)
    articles = category_data['articles']
    for article in articles:
        article['_id'] = str(article['_id'])  
    return jsonify({'category': category ,'articles': articles,'Categories': category_list })


@bp.route('/article/<string:article_id>')
def get_article_data(article_id):
    article_data = init_article(article_id)
    return jsonify({
        'Article': article_data['article'],
        'Related_articles' : article_data['related_articles']
    })

@bp.route('/article/<int:page>', methods=['GET'])
@bp.route('/article', defaults={'page': 1}, methods=['GET'])
def get_articles_by_tag(page):
    tag = request.args.get('tag') 
    tag_articles_data = retrive_articles_for_tag(tag, page=page)
    articles = tag_articles_data['articles']
    for article in articles:
        article['_id'] = str(article['_id'])
    return jsonify({'tag': tag, 'articles': articles})
