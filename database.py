import os
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

MONGO_URL = os.getenv("MONGO_DB_URL", None)

def build_mongo():
    mongo = MongoClient(MONGO_URL)
    return mongo.RES
    
db = build_mongo
