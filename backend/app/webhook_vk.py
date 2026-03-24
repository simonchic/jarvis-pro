from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
import requests
import random

# 🧠 Хранилище состояний пользователей
user_states = {}

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
    data = await request.json()
    print("WEBHOOK DATA:", data)

    # ✅ Подтверждение сервера
    if data.get("type") == "confirmation":
        return PlainTextResponse(content=CONFIRMATION_CODE)

    # ✅ Новое сообщение
    if data.get("type") == "message_new":
       user_id = data["object"]["message"]["from_id"]
       text = data["object"]["message"]["text"].lower()

       print(f"Новое сообщение от {user_id}: {text}")

    # если пользователь новый
    if user_id not in user_states:
        user_states[user_id] = {"step": None, "data": {}}

    state = user_states[user_id]

    # 🚀 старт
    if text == "участвовать":
        state["step"] = "name"
        send_message(user_id, "Представьтесь, кто вы?")
        return PlainTextResponse(content="ok")

    # 👤 кто вы
    if state["step"] == "name":
        state["data"]["name"] = text
        state["step"] = "city"
        send_message(user_id, "Какой город представляете?")
        return PlainTextResponse(content="ok")

    # 🌆 город
    if state["step"] == "city":
        state["data"]["city"] = text
        state["step"] = "nomination"
        send_message(user_id, "Какая у вас номинация?")
        return PlainTextResponse(content="ok")

    # 🎭 номинация
    if state["step"] == "nomination":
        state["data"]["nomination"] = text

        # 💥 финал + ссылка
        send_message(
            user_id,
            "Отлично 🙌\n\n"
            "Теперь пройдите по ссылке и заполните заявку:\n"
            "https://m.vk.com/app5708398_-189023036?ref=group_menu\n\n"
            "После отправки наши администраторы свяжутся с вами 📩"
        )

        # лог (чтобы ты видел заявки)
        print("ЗАЯВКА:", state["data"])

        # сброс
        user_states[user_id] = {"step": None, "data": {}}

        return PlainTextResponse(content="ok")

    # если не в сценарии
    send_message(
        user_id,
        "Напишите 'участвовать', чтобы подать заявку на фестиваль 🎭"
    )

    return PlainTextResponse(content="ok")

        # 🔥 AI
    from .core.ai import generate_answer
    answer = generate_answer(user_id, text)

        # 🔥 отправка
    send_message(user_id, answer)

    return PlainTextResponse(content="ok")

    # ✅ Все остальные события
    return PlainTextResponse(content="ok")