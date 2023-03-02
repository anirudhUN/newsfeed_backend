import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")
db=cluster["Newsfeed"]
source_collection=db["source"]
rssfeed_collection=db["rssData"]