from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Задаём код подтверждения VK
VK_CONFIRMATION_CODE = "4e2d9d86"

@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    """
    Основной обработчик событий VK
    """
    data = await request.json()
    print("WEBHOOK DATA:", data)

    # Проверка на подтверждение сервера
    if data.get("type") == "confirmation":
        return PlainTextResponse(VK_CONFIRMATION_CODE)

    # Обработка новых сообщений
    if data.get("type") == "message_new":
        # Здесь можно добавить обработку сообщений Джарвисом
        print("Новое сообщение от пользователя:", data["object"])
        return PlainTextResponse("ok")

    # По умолчанию просто "ok" для остальных событий
    return PlainTextResponse("ok")

@app.get("/")
def root():
    """
    Проверка, что сервер живой
    """
    return {"status": "JARVIS VK сервер работает"}