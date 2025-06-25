from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema
from app.db import init_db

clinical_app = FastAPI()

graphql_app = GraphQLRouter(schema)
clinical_app.include_router(graphql_app, prefix="/graphql")

@clinical_app.on_event("startup")
async def startup():
    await init_db()