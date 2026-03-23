from fastapi import FastAPI, Request
from starlette.responses import PlainTextResponse

app = FastAPI()

@app.post("/{full_path:path}")
async def vk_webhook_all(request: Request, full_path: str):
    data = await request.json()
    print("PATH:", full_path)
    print("DATA:", data)

    if data.get("type") == "confirmation":
        # 👇 ВАЖНО: именно str, не bytes
        return PlainTextResponse("2bca2318")

    return PlainTextResponse("ok")


@app.get("/")
def root():
    return {"status": "ok"}