from fastapi import FastAPI, Request
from starlette.responses import Response

app = FastAPI()

VK_CONFIRMATION_CODE = b"2bca2318"

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("WEBHOOK DATA:", data)

    # 👉 ТОЛЬКО ЧИСТЫЙ ОТВЕТ БЕЗ ВСЕГО
    if data.get("type") == "confirmation":
        return Response(
            content=VK_CONFIRMATION_CODE,
            media_type="text/plain",
            headers={"Content-Length": "8"}
        )

    return Response(content=b"ok", media_type="text/plain")


@app.get("/")
def root():
    return {"status": "ok"}