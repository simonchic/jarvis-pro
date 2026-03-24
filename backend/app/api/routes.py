from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from backend.app.vk_keyboard import get_main_keyboard

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("ДАННЫЕ:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse("1388031a", status_code=200)

    return PlainTextResponse("ok", status_code=200)