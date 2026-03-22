from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter()

VK_CONFIRMATION = "4e2d9d86"

@router.post("/webhook/vk")
async def vk_webhook(request: Request):
    data = await request.json()
    print("ДАННЫЕ:", data)

    # подтверждение сервера
    if data["type"] == "confirmation":
        print("ОТПРАВИТЬ ПОДТВЕРЖДЕНИЕ")
        return "10ac93"  # <- вставь новый код

    # новое сообщение
    if data["type"] == "message_new":
        user_id = data["object"]["message"]["from_id"]
        text = data["object"]["message"]["text"]

        answer = ask_ai(text)

        send_message(user_id, answer)

    return "ok"