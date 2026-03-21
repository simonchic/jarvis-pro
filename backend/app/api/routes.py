from fastapi import APIRouter, Request
from starlette.responses import Response

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    if data.get("type") == "confirmation":
        return Response(
            content=b"9cdbbfba",
            status_code=200,
            headers={
                "Content-Type": "text/plain"
            }
        )

    return Response(
        content=b"ok",
        status_code=200,
        headers={
            "Content-Type": "text/plain"
        }
    )