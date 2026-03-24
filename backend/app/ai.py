# backend/app/ai.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# память диалогов
user_histories = {}

def generate_answer(user_id: int, user_text: str) -> str:
    try:
        # если новый пользователь
        if user_id not in user_histories:
            user_histories[user_id] = [
                {
                    "role": "system",
                    "content": "Ты помощник фестиваля. Твоя задача — довести пользователя до подачи заявки. Общайся живо, задавай вопросы."
                }
            ]

        # добавляем сообщение пользователя
        user_histories[user_id].append({
            "role": "user",
            "content": user_text
        })

        # запрос к AI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=user_histories[user_id],
            temperature=0.7
        )

        answer = response.choices[0].message.content

        # сохраняем ответ
        user_histories[user_id].append({
            "role": "assistant",
            "content": answer
        })

        return answer

    except Exception as e:
        print("AI ERROR:", e)

        return "Ошибка AI ⚠️ Напишите 'участвовать'"