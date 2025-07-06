from fastapi import FastAPI
import asyncpg
import os

app = FastAPI()

DB_USER = "postgres"
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = "db"
DB_NAME = "postgres"

@app.get("/status")
async def status():
    return {"status": "ok"}

@app.get("/db")
async def db():
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASS,
                                 host=DB_HOST, database=DB_NAME)
    now = await conn.fetchval("SELECT NOW()")
    await conn.close()
    return {"db_time": str(now)}
