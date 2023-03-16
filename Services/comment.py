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

def get_comments(article_id, limit):
    article = trial_collection.find_one({'_id': ObjectId(article_id)})
    if article is None:
        return None
    comment = article['user_comments'][: limit]
    return comment

def get_one_comment(article_id, comment_index):
    article = trial_collection.find_one({'_id': ObjectId(article_id)})
    if article is None:
        return None
    comment = article['user_comments'][comment_index]
    return comment


def insert_comment(article_id, user_name, user_comment, time=datetime.utcnow()):
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

def delete_comments(article_id):
    article = trial_collection.find_one({'_id': ObjectId(article_id)})
    result = trial_collection.update_one({'_id': ObjectId(article_id)}, {'$unset': {'user_comments': [article['user_comments']]}})
    if result.matched_count == 1:
        return f"Comment deleted successfully from article_id: {article_id}"
    else:
        return f"Failed to delete comment from article_id: {article_id}"
    



'''
article_id = '64104d602ce733b171d9b0ed'
comment_index = 2
comment = get_one_comment(article_id, comment_index)
print(comment)
'''

'''
article_id = '64104d602ce733b171d9b0ed'
output = delete_comments(article_id)
print(output)
'''

'''
article_id = '64104d602ce733b171d9b0ed'
comment_index = 1
comment = delete_one_comment(article_id, comment_index)
print(comment)
'''


'''
article_id = '64104d5f2ce733b171d9b0ec'
user_name1 = 'Pratibha'
user_comment1 = 'The news is not trustworthy'
user_name2 = 'Bharat'
user_comment2 = 'Woahh technology is improving drastically. '
user_name3 = 'Kanika'
user_comment3 = 'Electric vehicles are gaining lot of popularity'

one = insert_comment(article_id, user_name1, user_comment1)
print(one)
two  = insert_comment(article_id, user_name2, user_comment2)
print(two) 
three  = insert_comment(article_id, user_name3, user_comment3)
print(three)
'''

'''
article_id = '64104d5f2ce733b171d9b0ec'
limit = COMMENT_COUNT
for comment in get_comments(article_id, limit):
    print(comment)

'''

