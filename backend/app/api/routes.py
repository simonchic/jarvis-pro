from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    if data.get("type") == "confirmation":
        return PlainTextResponse(content="9cdbbfba", media_type="text/plain")

    return PlainTextResponse(content="ok", media_type="text/plain")