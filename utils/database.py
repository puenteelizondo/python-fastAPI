# para crear una base de datos asincrona
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi





async def get_db():
    
    client = AsyncIOMotorClient("mongodb+srv://academia:academia@cluster0.rk0zhuw.mongodb.net/?retryWrites=true&w=majority")
    return client.academia
