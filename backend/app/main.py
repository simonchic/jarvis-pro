from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import logging
import json
import requests

# ==========================
# Настройка логирования
# ==========================
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

app = FastAPI()

# ==========================
# Ваши данные VK
# ==========================
CONFIRMATION_CODE = "1388031a"      # код подтверждения VK
GROUP_TOKEN = "aaQ13axAPQEcczQa"    # токен вашей группы VK

# URL для вызова методов VK API
VK_API_URL = "https://api.vk.com/method/"

# ==========================
# Основной webhook
# ==========================
@app.post("/webhook/vk")
async def vk_webhook(request: Request):
    """
    Обрабатываем все события VK.
    """
    try:
        data = await request.json()
    except Exception as e:
        logging.error(f"Ошибка при разборе JSON: {e}")
        return PlainTextResponse("Bad request", status_code=400)

    # Логируем все входящие события
    logging.info(f"WEBHOOK DATA: {json.dumps(data)}")

    # ==========================
    # Подтверждение сервера
    # ==========================
    if data.get("type") == "confirmation":
        logging.info("Запрос на подтверждение сервера VK")
        return PlainTextResponse(CONFIRMATION_CODE, status_code=200)

    # ==========================
    # Обработка новых сообщений
    # ==========================
    if data.get("type") == "message_new":
        message = data["object"]["text"]
        user_id = data["object"]["from_id"]
        logging.info(f"Новое сообщение от {user_id}: {message}")

        # Отправляем простой ответ через VK API
        send_message(user_id, f"Вы написали: {message}")

    # Всегда возвращаем 200 OK, чтобы VK не считал запрос неуспешным
    return PlainTextResponse("ok", status_code=200)

# ==========================
# Функция для отправки сообщений
# ==========================
def send_message(user_id: int, message: str):
    """
    Отправка сообщения пользователю через VK API
    """
    payload = {
        "user_id": user_id,
        "message": message,
        "access_token": GROUP_TOKEN,
        "v": "5.199"
    }
    try:
        response = requests.post(VK_API_URL + "messages.send", data=payload)
        result = response.json()
        if "error" in result:
            logging.error(f"Ошибка VK при отправке сообщения: {result['error']}")
        else:
            logging.info(f"Сообщение успешно отправлено пользователю {user_id}")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")