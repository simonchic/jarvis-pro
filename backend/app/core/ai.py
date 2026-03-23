import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(user_text: str) -> str:
    """
    Генерация ответа от Джарвиса
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Ты умный помощник фестиваля. Отвечай кратко, понятно и помогай пользователю записаться."
            },
            {
                "role": "user",
                "content": user_text
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content