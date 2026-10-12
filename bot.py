import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# Apna Discord Token aur Channel ID yahan daalein
TOKEN = "MTUzNzQwOTI1MjcwNzAxMjcwMA.GsNw7I.ipvjQmTcx0e5KYk8gEobAVic-VJhG7f100nIzY"
CHANNEL_ID = "1410924658840178738"
my_paragraph = "Trading psychology is the blend of emotions, mental states, and behavioral biases that steer how a person makes decisions in financial markets."

@app.route('/')
def home():
    return "Discord Bot is running 24/7!"

def send_messages():
    print("Background worker started!")
    time.sleep(5)  # Thoda wait karega taaki server fully start ho jaye
    
    while True:
        url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
        headers = {
            "Authorization": TOKEN,
            "Content-Type": "application/json"
        }
        payload = {
            "content": my_paragraph
        }
        try:
            print("Sending message to Discord...")
            response = requests.post(url, json=payload, headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print("Exception error:", e)
        
        # Har 5 minute (300 seconds) baad message bhejega
        print("Waiting for 5 minutes...")
        time.sleep(300)

if __name__ == "__main__":
    # Background thread mein message sender start karenge
    t = threading.Thread(target=send_messages, daemon=True)
    t.start()
    
    # Render ke liye Flask web server port 10000 par chalayenge
    app.run(host='0.0.0.0', port=10000)
