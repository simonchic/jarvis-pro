# backend/app/ai.py

import os
from openai import OpenAI

# 🔑 Инициализация клиента
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 Хранилище диалогов (в памяти)
user_histories = {}


def generate_answer(user_id: int, user_text: str) -> str:
    """
    Генерация ответа с учетом истории диалога
    """

    try:
        # если новый пользователь — создаём историю
        if user_id not in user_histories:
            user_histories[user_id] = [
                {
                    "role": "system",
                    "content": (
                        "Ты менеджер по продажам фестиваля. Твоя цель — довести человека до подачи заявки. Общайся просто, задавай вопросы, закрывай возражения."
                    )
                }
            ]

        # добавляем сообщение пользователя
        user_histories[user_id].append({
            "role": "user",
            "content": user_text
        })

        # 🔥 запрос к OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=user_histories[user_id],
            temperature=0.7
        )

        answer = response.choices[0].message.content

        # сохраняем ответ в историю
        user_histories[user_id].append({
            "role": "assistant",
            "content": answer
        })

        return answer

    except Exception as e:
        print("AI ERROR:", e)

        # 👇 fallback ответ
        return (
            "Сейчас есть небольшая нагрузка 🙏\n"
            "Напишите 'участвовать', и я помогу вам подать заявку на фестиваль."
        )