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

def content_scraping(driver,collection):
    for doc in collection.find():
            article_url = doc['link']
            article_source=doc['Source']
            driver.get(article_url)
            for source,selector in SOURCE_SELECTOR_MAPPER.items():
                 if source==article_source:
                        try:
                            wait = WebDriverWait(driver, 20)
                            article = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                            content=article.text
                            collection.update_one({'_id': doc['_id']}, {'$set': {'article-content': content}})
                        except (NoSuchElementException, Exception) as e:
                            print(f"Error occurred while retrieving article content for {article_url}: {e}")    

if __name__=="__main__":
     content_scraping(driver,article_collection)       