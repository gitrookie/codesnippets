# testmongo.py
# A mongodb client
from pymongo import MongoClient

client = MongoClient()
db = client["primer"]
