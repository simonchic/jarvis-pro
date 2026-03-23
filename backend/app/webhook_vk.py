from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
import requests
import random

VK_TOKEN = "vk1.a.g4hjBYC45Pz15v9acgA44KNHcqzIz6c7z1UOfNVNgc-sJGQVfeoUzAC4FNhj4TXXdi07cfsX4t3Gggc8_f843JcDnWZ0LEBPD49Wn8Rpt0hKelZ1XPoJkipgCukZR_B5hwkIedtXUknjo8FA4qha4-20U6aEPWF6EMMeNBJwbpdx5HN1_lOeNixpXQ_tNGcWPeAz1Pucno7OWj7Um59i7g"

def send_message(user_id, text):
    requests.post(
        "https://api.vk.com/method/messages.send",
        params={
            "user_id": user_id,
            "message": text,
            "random_id": random.randint(1, 1_000_000),
            "access_token": VK_TOKEN,
            "v": "5.199",
        },
    )
router = APIRouter()

# Твой код подтверждения из ВК
CONFIRMATION_CODE = "1388031a"

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    """
    Обрабатываем POST-запросы от VK.
    Сначала приходит 'confirmation', чтобы подтвердить сервер.
    Потом приходят события, например, новые сообщения.
    """
    data = await request.json()
    print("WEBHOOK DATA:", data)

    # Если VK присылает подтверждение
    if data.get("type") == "confirmation":
        # Возвращаем именно код подтверждения
        return PlainTextResponse(content=CONFIRMATION_CODE)

    # Если событие, например, новое сообщение
    if data.get("type") == "message_new":
       user_id = data["object"]["message"]["from_id"]
       text = data["object"]["message"]["text"]

    print(f"Новое сообщение от {user_id}: {text}")

    # 🔥 подключаем AI
    from .core.ai import generate_answer

    # 🔥 получаем ответ с памятью
    answer = generate_answer(user_id, text)

    # 🔥 отправляем сообщение
    from .vk_send_message import send_message
    send_message(user_id, answer)

    return PlainTextResponse(content="ok")

    send_message(user_id, "Привет! 👋 Заявка на фестиваль: напиши 'участвовать'")

    return PlainTextResponse(content="ok")

    # Для всех остальных событий просто возвращаем 'ok'
    return PlainTextResponse(content="ok")