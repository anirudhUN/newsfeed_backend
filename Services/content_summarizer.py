import nltk
import numpy as np
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

nltk.download('punkt')

def init_summary(article_id, article_content):     
    sentences = nltk.sent_tokenize(article_content)
    scores = np.array([len(nltk.word_tokenize(s)) for s in sentences])
    idx = scores.argsort()[::-1]
    summary = '\n'.join([sentences[i] for i in sorted(idx[:3])])
    article_collection.update_one({'_id': article_id}, {'$set': {'summary': summary}})

