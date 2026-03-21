from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from backend.app.core.ai import ask_ai
from backend.app.core.memory import save, get
from backend.app.integrations.vk import send_message
import os

router = APIRouter()

# ❗ ВРЕМЕННО ВСТАВЛЯЕМ ЖЁСТКО (чтобы точно заработало)
VK_CONFIRMATION = "4aea2e2f"


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


# ✅ ВАЖНО: webhook ДОЛЖЕН БЫТЬ СНАРУЖИ
@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    print("VK WEBHOOK HIT")

    data = await request.json()
    print("VK DATA:", data)

    if data["type"] == "confirmation":
        return PlainTextResponse("c0740fbf")

    if data["type"] == "message_new":
        user_id = data["object"]["message"]["from_id"]
        text = data["object"]["message"]["text"]

        answer = ask_ai(text)
        send_message(user_id, answer)

    return PlainTextResponse("ok")

    # подтверждение сервера
    if data["type"] == "confirmation":
        print("CONFIRMATION SENT")
        return "c0740fbf"

    # новое сообщение
    if data["type"] == "message_new":
        user_id = data["object"]["message"]["from_id"]
        text = data["object"]["message"]["text"]

        answer = ask_ai(text)

        send_message(user_id, answer)

    return "ok"