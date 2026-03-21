from fastapi import APIRouter, Request
from pydantic import BaseModel
from backend.app.core.ai import ask_ai
from backend.app.core.memory import save, get
from backend.app.integrations.vk import send_message
import os

router = APIRouter()

VK_CONFIRMATION = os.getenv("VK_CONFIRMATION")


class ChatRequest(BaseModel):
    user_id: str
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    try:
        save(req.user_id, req.message)

        history = get(req.user_id)
        full_text = "\n".join(history[-5:])

        answer = ask_ai(full_text)

        save(req.user_id, answer)

        return {"response": answer}

    except Exception as e:
        print("Ошибка /chat:", e)
        return {"response": "Ошибка сервера"}


# ❗ ВАЖНО: webhook отдельно
@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()

    print("VK DATA:", data)  # для логов

    # подтверждение сервера
    if data["type"] == "confirmation":
        return VK_CONFIRMATION

    # новое сообщение
    if data["type"] == "message_new":
        user_id = data["object"]["message"]["from_id"]
        text = data["object"]["message"]["text"]

        answer = ask_ai(text)

        send_message(user_id, answer)

    return "ok"