import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from Services.home import *
from bson import ObjectId
from flask import Flask, jsonify
from jsonschema import validate

app = Flask(__name__)

@app.route('/home')
def get_home_data():
    home_data = init_home_page(article_collection,page=None)
    articles = home_data['articles']
    for article in articles:
        article['_id'] = str(article['_id'])  # convert ObjectId to string
    return jsonify({
        'categories': home_data['categories'],
        'articles': articles
    })

