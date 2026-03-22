from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

CONFIRMATION_TOKEN = "4e2d9d86"

# 👉 VK может бить сюда
@app.post("/")
async def vk_root(request: Request):
    data = await request.json()
    print("ROOT DATA:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse(CONFIRMATION_TOKEN)

    return PlainTextResponse("ok")


# 👉 и сюда
@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("WEBHOOK DATA:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse(CONFIRMATION_TOKEN)

    return PlainTextResponse("ok")


@app.get("/")
def root():
    return {"status": "JARVIS работает"}