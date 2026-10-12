import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

TOKEN = "MTUzNzQwOTI1MjcwNzAxMjcwMA.GsNw7I.ipvjQmTcx0e5KYk8gEobAVic-VJhG7f100nIzY"
CHANNEL_ID = "1410924658840178738"
my_paragraph = "Trading psychology is the blend of emotions, mental states, and behavioral biases that steer how a person makes decisions in financial markets."

@app.route('/')
def home():
    return "Discord Bot is running 24/7!"

def send_messages():
    print("Background worker thread started successfully!")
    time.sleep(2)
    
    while True:
        url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
        
        # Yahan humne real browser ka User-Agent add kiya hai taaki block na ho
        headers = {
            "Authorization": TOKEN,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        payload = {
            "content": my_paragraph
        }
        
        try:
            print(">>> Sending message request to Discord API...")
            response = requests.post(url, json=payload, headers=headers)
            print(f">>> STATUS CODE: {response.status_code}")
            print(f">>> RESPONSE TEXT: {response.text}")
        except Exception as e:
            print(">>> Exception error:", e)
        
        print(">>> Waiting for 5 minutes before next message...")
        time.sleep(300)

def start_background_task():
    t = threading.Thread(target=send_messages, daemon=True)
    t.start()

start_background_task()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
