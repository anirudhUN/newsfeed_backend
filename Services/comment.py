import sys
import os
from datetime import datetime
from bson import ObjectId

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *
from datetime import datetime

trial_collection=database[TRIAL_COLLECTION]

def update_comment(article_id, user_name, user_comment, time=datetime.utcnow()):
    user_comment = {'user_name': user_name, 'user_comment': user_comment, 'time': time}
    article = trial_collection.find_one({'_id': ObjectId(article_id)})
    if 'user_comments' in article:
        if isinstance(article['user_comments'], list):
            result = trial_collection.update_one({'_id': ObjectId(article_id)}, {'$push': {'user_comments': user_comment}})
            if result.matched_count == 1:
                return f"Comment added successfully for article_id: {article_id}"
            else:
                return f"Failed to add comment for article_id: {article_id}"
        else:
            trial_collection.update_one({'_id': ObjectId(article_id)}, {'$set': {'user_comments': [article['user_comments'], user_comment]}})
            return f"Comment added successfully for article_id: {article_id}"
    else:
        trial_collection.update_one({'_id': ObjectId(article_id)}, {'$set': {'user_comments': [user_comment]}})
        return f"Comment added successfully for article_id: {article_id}"

'''
article_id = '64104d602ce733b171d9b0ed'
user_name1 = 'Bhaskar'
user_comment1 = 'The news is not trustworthy'
user_name2 = 'Sweety'
user_comment2 = 'Woahh technology is improving drastically. '

one = update_comment(article_id, user_name1, user_comment1)
print(one)
two  = update_comment(article_id, user_name2, user_comment2)
print(two) 
'''