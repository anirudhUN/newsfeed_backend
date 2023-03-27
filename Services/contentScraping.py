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
            source_selectors = SOURCE_SELECTOR_MAPPER.get(article_source)
            if source_selectors is None:
                continue
            try:
                wait = WebDriverWait(driver, 20)
                article = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, source_selectors['article'])))
                content = article.text

                try:
                    # scrape tags
                    tags = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, source_selectors['tags'])))
                    tags_data = []
                    for tag in tags:
                        tag_name = tag.text
                        tag_link = tag.get_attribute('href')
                        tags_data.append({'name': tag_name, 'link': tag_link}) 
                        
                except NoSuchElementException:
                    tags_data = ""                              
            
                try:
                    # scrape image
                    image_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, source_selectors['image'])))
                    image_url = image_element.get_attribute('src')
                    
                except NoSuchElementException:
                    image_url = ""

                collection.update_one({'_id': doc['_id']}, {'$set': {'article-content': content,'tags': tags_data,'image-url': image_url}})

            except (NoSuchElementException, Exception) as e:
                print(f"Error occurred while retrieving article content for {article_url}: {e}") 
                           
if __name__=="__main__":
     content_scraping(driver,article_collection)