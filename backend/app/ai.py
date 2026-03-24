# backend/app/ai.py

from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.neuroapi.host/v1"  # 🔥 ВАЖНО
)

def generate_answer(user_id, text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # можно менять если не работает
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты менеджер творческого фестиваля. "
                        "Отвечай дружелюбно, просто и по делу. "
                        "Помогай и мягко веди к подаче заявки."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI ERROR:", e)
        return "⚠️ AI временно недоступен. Напишите чуть позже."