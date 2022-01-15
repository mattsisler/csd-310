#Sisler - Module 5.2 Assignment
#Mongo DB Test Connection
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.h1wgd.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List --")
print(db.list_collection_names())
input("End of Program. Press any key to continue")
