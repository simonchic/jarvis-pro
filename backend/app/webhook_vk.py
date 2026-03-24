from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
import requests
import random
import json
import os

from backend.app.ai import generate_answer

router = APIRouter()

VK_TOKEN = os.getenv("VK_TOKEN")
CONFIRMATION_CODE = "1388031a"

user_states = {}

def get_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "📥 Подать заявку"}, "color": "primary"}],
            [{"action": {"type": "text", "label": "💰 Рассчитать стоимость"}, "color": "positive"}],
            [{"action": {"type": "text", "label": "📞 Связаться"}, "color": "secondary"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

def send_message(user_id, text):
    requests.post(
        "https://api.vk.com/method/messages.send",
        params={
            "user_id": user_id,
            "message": text,
            "random_id": random.randint(1, 1_000_000),
            "access_token": VK_TOKEN,
            "v": "5.199",
            "keyboard": get_keyboard()
        }
    )

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    # ✅ подтверждение VK
    if data.get("type") == "confirmation":
        return PlainTextResponse(content=CONFIRMATION_CODE)

    # ✅ ОБРАБАТЫВАЕМ ТОЛЬКО СООБЩЕНИЯ
    if data.get("type") != "message_new":
        return PlainTextResponse(content="ok")

    message = data["object"]["message"]
    user_id = message["from_id"]
    text = message.get("text", "").strip()

    # создаём состояние пользователя
    if user_id not in user_states:
        user_states[user_id] = {"step": None, "data": {}}

    state = user_states[user_id]

    # =========================
    # 🔘 КНОПКИ (главное меню)
    # =========================

    if text == "📥 Подать заявку":
        state["step"] = "name"
        send_message(user_id, "Давайте оформим заявку 🎭\n\nКак вас зовут?")
        return PlainTextResponse(content="ok")

    if text == "💰 Рассчитать стоимость":
        send_message(user_id, "Напишите, сколько участников и номинацию — я рассчитаю 💰")
        return PlainTextResponse(content="ok")

    if text == "📞 Связаться":
        send_message(user_id, "Напишите ваш вопрос, и я передам организатору 📩")
        return PlainTextResponse(content="ok")

    # =========================
    # 📋 СЦЕНАРИЙ ЗАЯВКИ
    # =========================

    if state["step"] == "name":
        state["data"]["name"] = text
        state["step"] = "city"
        send_message(user_id, "Из какого вы города?")
        return PlainTextResponse(content="ok")

    if state["step"] == "city":
        state["data"]["city"] = text
        state["step"] = "nomination"
        send_message(user_id, "Какая у вас номинация?")
        return PlainTextResponse(content="ok")

    if state["step"] == "nomination":
        state["data"]["nomination"] = text

        send_message(
            user_id,
            f"Заявка принята ✅\n\n"
            f"👤 {state['data']['name']}\n"
            f"🏙 {state['data']['city']}\n"
            f"🎭 {state['data']['nomination']}"
        )

        # сброс
        user_states[user_id] = {"step": None, "data": {}}
        return PlainTextResponse(content="ok")

    # =========================
    # 🤖 AI (если не кнопка)
    # =========================

    answer = generate_answer(user_id, text)
    send_message(user_id, answer)

    return PlainTextResponse(content="ok")