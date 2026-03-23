from fastapi import FastAPI, Request, Response

app = FastAPI()

VK_CONFIRMATION_CODE = "2bca2318"

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("WEBHOOK DATA:", data)

    if data.get("type") == "confirmation":
        return Response(
            content=b"2bca2318",
            media_type="text/plain"
        )

    if data.get("type") == "message_new":
        print("Новое сообщение:", data["object"])
        return Response(content=b"ok", media_type="text/plain")

    return Response(content=b"ok", media_type="text/plain")


@app.get("/")
def root():
    return {"status": "JARVIS VK сервер работает"}