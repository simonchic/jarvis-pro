from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter()

VK_CONFIRMATION = "10ac93d4"

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    print("VK DATA:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse(VK_CONFIRMATION)

    return PlainTextResponse("ok")