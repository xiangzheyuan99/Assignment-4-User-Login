from pymongo import AsyncMongoClient
from beanie import init_beanie
import os
from dotenv import load_dotenv
from models.user import User

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

async def init_db():
    client = AsyncMongoClient(MONGODB_URL)
    database = client.get_default_database()
    await init_beanie(database=database, document_models=[User])