import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://anirudhaun:cY5hdsdwvg1aHTex@cluster0.suvfptn.mongodb.net/?retryWrites=true&w=majority")
db=cluster["Newsfeed"]
source_collection=db["Collection"]
rssfeed_collection=db["rssCollection"]