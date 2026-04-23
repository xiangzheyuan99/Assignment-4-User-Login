from fastapi import FastAPI
from database.connection import init_db
from routes.users import user_router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["user"])

@app.on_event("startup")
async def startup():
    await init_db()
    logger.info("Database connected successfully")

@app.get("/")
async def root():
    return {"message": "App is running"}

@app.get("/dashboard")
async def dashboard():
    return {"message": "Welcome to the dashboard"}