from fastapi import APIRouter, Request
from starlette.responses import Response

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    body = await request.body()
    print("RAW BODY:", body)

    data = await request.json()
    print("DATA:", data)

    if data.get("type") == "confirmation":
        return Response(
            content="9cdbbfba",
            media_type="text/plain; charset=utf-8"
        )

    return Response(
        content="ok",
        media_type="text/plain; charset=utf-8"
    )