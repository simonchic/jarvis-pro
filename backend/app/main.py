from fastapi import FastAPI, Request
from starlette.responses import Response

app = FastAPI()

VK_CONFIRMATION_CODE = b"2bca2318"

# 👉 ЛОВИМ ВСЕ POST ЗАПРОСЫ
@app.post("/{full_path:path}")
async def vk_webhook_all(request: Request, full_path: str):
    data = await request.json()
    print("PATH:", full_path)
    print("DATA:", data)

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