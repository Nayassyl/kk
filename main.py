from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import create_tables, delete_tables
from router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Creating tables...") 
    await create_tables()
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(router)

tasks = []
@app.get("/")
def root():
    return {"status": "ok"} 