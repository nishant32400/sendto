from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "jocflightdb_30jan")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "flight")

_client = MongoClient(MONGO_URI)
collection = _client[MONGO_DB][MONGO_COLLECTION]

def get_collection():
    return collection
