# backend/app/main.py
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from backend.app.webhook_vk import router as vk_router  # ✅ ВАЖНО

app = FastAPI()
app.include_router(vk_router)

@app.get("/")
async def root():
    return {"status": "server is running"}