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



class HOME():
    def __init__(self):
        self.category = []
    def get_category(self, categories):
        self.category.extend(categories)

@app.route('/category')
def get_data():
    data = []
    categories = get_categories(article_collection)
    home = HOME()
    home.get_category(categories)
    data.append({
        'category' : home.category
        })
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)