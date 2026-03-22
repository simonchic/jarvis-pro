from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
def root():
    return {"status": "JARVIS работает"}

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("WEBHOOK DATA:", data)

    # Подтверждение адреса для VK
    if data.get("type") == "confirmation":
        # Возвращаем строго plain text без кавычек, JSON и лишних символов
        return Response(content="4e2d9d86", media_type="text/plain; charset=utf-8")

    # Для всех остальных событий VK
    return Response(content="ok", media_type="text/plain; charset=utf-8")