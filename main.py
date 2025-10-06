from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    env = os.getenv("ENV_NAME", "unknown")
    return {"message": f"Hello from FastAPI! Running in {env} environment"}