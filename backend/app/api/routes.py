from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("ДАННЫЕ:", data)

    if data.get("type") == "confirmation":
        return "4e2d9d86"

    return "ok"