# backend/app/ai.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 Хранилище диалогов (в памяти)
user_histories = {}


def generate_answer(user_id: int, user_text: str) -> str:
    """
    Генерация ответа с учетом истории диалога
    """

    # если новый пользователь — создаём историю
    if user_id not in user_histories:
        user_histories[user_id] = [
            {
                "role": "system",
                "content": "Ты умный помощник фестиваля. Твоя задача — довести пользователя до подачи заявки. Задавай вопросы и веди диалог."
            }
        ]

    # добавляем сообщение пользователя
    user_histories[user_id].append({
        "role": "user",
        "content": user_text
    })

    # отправляем в AI
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