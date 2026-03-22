from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("ДАННЫЕ:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse("4e2d9d86")

    return PlainTextResponse("ok")