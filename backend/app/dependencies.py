from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb://mongo:27017")
db = client["bibliotheque"]

def get_books_collection() -> Collection:
    return db["books"]

def get_users_collection() -> Collection:
    return db["users"]
