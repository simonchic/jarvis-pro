from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
import os

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    if data.get("type") == "confirmation":
        return PlainTextResponse(os.getenv("VK_CONFIRMATION"))

    return PlainTextResponse("ok")