# backend/app/vk_send_message.py
import requests
import random

# Токен группы VK (замени на свой)
VK_TOKEN = "vk1.a.g4hjBYC45Pz15v9acgA44KNHcqzIz6c7z1UOfNVNgc-sJGQVfeoUzAC4FNhj4TXXdi07cfsX4t3Gggc8_f843JcDnWZ0LEBPD49Wn8Rpt0hKelZ1XPoJkipgCukZR_B5hwkIedtXUknjo8FA4qha4-20U6aEPWF6EMMeNBJwbpdx5HN1_lOeNixpXQ_tNGcWPeAz1Pucno7OWj7Um59i7g"

def send_message(user_id, text):
    """
    Отправляет сообщение пользователю через VK API.
    """
    requests.post(
        "https://api.vk.com/method/messages.send",
        params={
            "user_id": user_id,
            "message": text,
            "random_id": random.randint(1, 1_000_000),
            "access_token": VK_TOKEN,
            "v": "5.199",
        },
    )