import os
import requests
from dotenv import load_dotenv
load_dotenv()
# Get the bot token and channel ID from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = "-1001509235658"
print(TOKEN)

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()


if __name__ == '__main__':
    message = "Hello scheduled!!!"
    response = send_message(TOKEN, CHANNEL_ID, message)
    print(response)
