from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

VK_CONFIRMATION_CODE = "2bca2318"

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("WEBHOOK DATA:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse(VK_CONFIRMATION_CODE)

    if data.get("type") == "message_new":
        print("Новое сообщение:", data["object"])
        return PlainTextResponse("ok")

    return PlainTextResponse("ok")

@app.get("/")
def root():
    return {"status": "JARVIS VK сервер работает"}