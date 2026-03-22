from fastapi import FastAPI, Request
from starlette.responses import Response

app = FastAPI()

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("RAW DATA:", data)

    if data.get("type") == "confirmation":
        return Response(
            content=b"4e2d9d86",
            media_type="text/plain"
        )

    return Response(content=b"ok", media_type="text/plain")


@app.get("/")
def root():
    return {"status": "JARVIS работает"}