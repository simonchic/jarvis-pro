from fastapi import APIRouter, Request
from fastapi.responses import Response

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("ДАННЫЕ:", data)

    if data.get("type") == "confirmation":
        return Response(content="4e2d9d86", media_type="text/plain")

    return Response(content="ok", media_type="text/plain")