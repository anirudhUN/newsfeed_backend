import pymongo
from pymongo import MongoClient
from db_properties import *


#post1={"Source":"TechCrunch","Title":"Tesla raises price of Full Self-Driving option to $10k","Summary":"Tesla has raised the price of its Full Self-Driving option to $10,000 ...","ArticleContent":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod...","AuthorNames":["John Doe"],"ArticleURL":"https://techcrunch.com/2021/02/08/tesla-raises-price-of-full-self-driving-option-to-10k/","CoverImgURL":"https://img.techcrunch.com/2021/02/08/tesla-model-s-red.jpg","Tags":["Tesla","Self-Driving","Autonomous Vehicles"],"Comments":["Great news for Tesla investors!","I can't afford this."],"Category":"Technology"}
#post2={"Source":"The Verge","Title":"Microsoft releases emergency update to fix Windows 10 bug causing blue screens","Summary":"Microsoft is releasing an emergency update to its Windows 10 operating system...","ArticleContent":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod...","AuthorNames":["Bob Johnson"],"ArticleURL":"https://www.theverge.com/2021/2/9/22274814/microsoft-windows-10-emergency-update-blue-screen-bug-fix","CoverImgURL":"https://cdn.vox-cdn.com/thumbor/rzh_-QsO4fZ4q-V6jhgeBvmt-K8=/0x0:2040x1360/920x613/filters:focal(860x1096:1180x1416):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/68950562/acastro_210205_1777_windows10_0006.0.jpg","Tags":["Microsoft","Windows 10","Bug"],"Comments":["Glad they're addressing this quickly.","Another reason to switch to Linux!"],"Category":"Technology"}
#post3={"Source":"TechCrunch","Title":"New MacBook Pro expected to launch in coming months","Summary":"Apple is expected to launch a new MacBook Pro model in the coming months...","ArticleContent":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod...","AuthorNames":["Jane Doe"],"ArticleURL":"https://techcrunch.com/2023/02/09/new-macbook-pro-expected-to-launch-in-coming-months/","CoverImgURL":"https://img.techcrunch.com/2023/02/09/macbook-pro.jpg","Tags":["Apple","MacBook Pro","Laptops"],"Comments":["Excited to see what new features it will have!","I just bought a MacBook Pro, should I return it?"],"Category":"Technology"}
#collection.insert_many([post1,post2,post3])
#result= collection.find()

#function to get a list of categories
def getcategories():
    categories = source_collection.distinct('category')
    for category in categories:
        print(category)
#getcategories()

#to get a particular category of results
def getcatnews(category):
        results=source_collection.find({"Category":category},{})
        for i in results:
            print(i)
#getcatnews("Technology")

#to get results relating to a particular tag
def gettagnews(tag):
      results=source_collection.find({"Tags":tag},{})
      for i in results:
            print(i)
#gettagnews("Apple")

#to get articles from a particular source
def getsourcenews(source):
      results=source_collection.find({"Source":source},{})
      for i in results:
            print(i)
#getsourcenews("TechCrunch")

#toget a list of sources
def getsources():
      results=source_collection.distinct("Source")
      for i in results:
            print(i)
#getsources()

def get_article_details():
    
    # Find the 10 most recent articles in the collection
    articles = source_collection.find().sort('Timestamp', -1).limit(10)
    
    # Loop through the articles and extract the details
    article_details = []
    for article in articles:
        details = {
            'title': article['Title'],
            'summary': article['Summary'],
            'image_url': article['CoverImgURL'],
            'source': article['Source'],
            'tags': article['Tags']
        }
        article_details.append(details)
        
    # Return the list of article details
    for articles in article_details:
         print(article)
get_article_details() 

