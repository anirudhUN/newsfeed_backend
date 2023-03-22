import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from properties.db_properties import *
from utils.mongo_utils import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Chrome(PATH)

def article_content_scraping(driver,collection):
    query = {"Source": "Hackaday"}
    for doc in collection.find(query):
        article_url=doc['link']
        driver.get(article_url)
        try:
            wait = WebDriverWait(driver, 20)
            article = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.entry-content")))
            content=article.text
            collection.update_one({'_id': doc['_id']}, {'$set': {'article-content': content}})
        except (NoSuchElementException, Exception) as e:
            print(f"Not able to access {article_url}: {e}")

if __name__=="__main__":
     article_content_scraping(driver,article_collection)