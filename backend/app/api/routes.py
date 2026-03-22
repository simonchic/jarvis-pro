from fastapi import APIRouter, Request
from starlette.responses import Response

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    if data.get("type") == "confirmation":
        return Response(
            content=b"cfe77b44",
            media_type="text/plain"
        )

    return Response(content=b"ok", media_type="text/plain")