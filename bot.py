import time
import threading
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running 24/7!")

def run_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHandler)
    server.serve_forever()

# Apna Discord Token aur Channel ID yahan dalein
TOKEN = "MTUzNzQwOTI1MjcwNzAxMjcwMA.GsNw7I.ipvjQmTcx0e5KYk8gEobAVic-VJhG7f100nIzY"
CHANNEL_ID = "1410924658840178738"
my_paragraph = "Trading psychology is the blend of emotions, mental states, and behavioral biases that steer how a person makes decisions in financial markets."

def send_messages():
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
            response = requests.post(url, json=payload, headers=headers)
            print(f"Status Code: {response.status_code}")
        except Exception as e:
            print("Exception:", e)
        
        # Har 5 minute (300 seconds) baad message bhejega
        time.sleep(300)

if __name__ == "__main__":
    t = threading.Thread(target=send_messages)
    t.daemon = True
    t.start()
    
    run_server()   
    
