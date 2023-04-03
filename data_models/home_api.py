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
    
@app.route('/home')
def get_data():
    data = []
    page = 1 #write post method 
    articles = get_successive_articles(article_collection,page)
    for record in articles:
        home = HOME()
        data.append({
            'id': str(record['_id']),
            'title': str(record['title']),
            'source ': str(record.get('Source', '')),
            'image-url': str(record.get('image-url', '')),
            'published': str(record.get('published', '')), 
            'summary':  str(record.get('summary', '')), 
            'tags':  str(record.get('tags', ''))
        })
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
