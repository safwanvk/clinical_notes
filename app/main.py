from fastapi import FastAPI
from app.db import init_db

clinical_app = FastAPI()

@clinical_app.on_event("startup")
async def startup():
    await init_db()