import os
from dotenv import load_dotenv
from openai import OpenAI

# загружаем .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Ты — JARVIS, умный ассистент.

Ты работаешь для творческого фестиваля.

Отвечай ВСЕГДА на русском языке.

Твои задачи:
- отвечать участникам
- помогать с заявками
- объяснять условия участия
- писать тексты и посты
- быть вежливым и уверенным

Отвечай понятно, без сложных слов, как живой человек.
"""

def ask_ai(text):
    return "Тестовый ответ"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content or "Нет ответа"

    except Exception as e:
        print("Ошибка AI:", e)
        return "Произошла ошибка при обращении к AI"