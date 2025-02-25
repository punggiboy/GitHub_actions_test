import asyncio 
from fastapi import FastAPI 

app = FastAPI()

async def fetch_data():
    await asyncio.sleep(2)
    return {"data":"some data"}

@app.get("/")
async def read_root():
    data = await fetch_data()
    return {"message": "Hello, World!", "fetch_data":data}


