from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URL", "mongodb://mongo:27017"))
db = client.biblio
users = db.users
books = db.books