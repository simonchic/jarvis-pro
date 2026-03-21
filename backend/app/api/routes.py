from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    print("=== VK WEBHOOK HIT ===")

    data = await request.json()
    print("DATA:", data)

    if data.get("type") == "confirmation":
        print("SENDING CONFIRM")
        return PlainTextResponse("9cdbbfba")

    return PlainTextResponse("ok")