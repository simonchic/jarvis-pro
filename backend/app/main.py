from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("MAIN DATA:", data)

    if data.get("type") == "confirmation":
        return PlainTextResponse("4e2d9d86")

    return PlainTextResponse("ok")


@app.get("/")
def root():
    return {"status": "JARVIS работает"}