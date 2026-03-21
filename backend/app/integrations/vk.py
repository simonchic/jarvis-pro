import os
import requests
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
VK_API_URL = "https://api.vk.com/method/messages.send"
VK_VERSION = "5.199"

def send_message(user_id, message):
    requests.post(VK_API_URL, params={
        "user_id": user_id,
        "message": message,
        "random_id": 0,
        "access_token": VK_TOKEN,
        "v": VK_VERSION
    })