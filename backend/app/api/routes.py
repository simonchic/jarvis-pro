from fastapi import APIRouter, Request
from starlette.responses import Response
import os

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    # ✅ подтверждение VK
    if data.get("type") == "confirmation":
        return Response(
            content=os.getenv("VK_CONFIRMATION"),
            status_code=200,
            media_type="text/plain"
        )

    # ✅ чтобы VK не ругался
    return Response(content="ok", media_type="text/plain")