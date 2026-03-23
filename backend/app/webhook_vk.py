from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

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
        user_id = data["object"]["from_id"]
        text = data["object"]["text"]
        print(f"Новое сообщение от {user_id}: {text}")
        # Здесь можно добавить обработку или ответ пользователю через VK API
        return PlainTextResponse(content="ok")

    # Для всех остальных событий просто возвращаем 'ok'
    return PlainTextResponse(content="ok")