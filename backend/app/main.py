# backend/app/main.py

# 1️⃣ Импортируем FastAPI и наш роутер для VK
from fastapi import FastAPI
from .webhook_vk import router as vk_router  # <-- здесь подключаем webhook_vk.py

# 2️⃣ Создаём сервер FastAPI
app = FastAPI()

# 3️⃣ Подключаем роутер VK
app.include_router(vk_router)

# 4️⃣ Тестовый маршрут, чтобы проверить, что сервер работает
@app.get("/")
async def root():
    return {"status": "server is running"}