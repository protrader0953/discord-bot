import time
import random
import threading
import requests
from flask import Flask

app = Flask(__name__)

# Aapka Personal Discord User Token
USER_TOKEN = "MTUzNzQwOTI1MjcwNzAxMjcwMA.GsNw7I.ipvjQmTcx0e5KYk8gEobAVic-VJhG7f100nIzY"

# Target Channel ID
CHANNEL_ID = "1214041131976691763"

# Trading Paragraphs List
paragraphs = [
    "Order flow analysis gives traders a deeper look into the actual buying and selling transactions taking place in real time. Instead of relying solely on completed candlestick patterns, order flow tools like footprint charts and the depth of market show where volume is being absorbed and where aggressive market orders are entering. Understanding whether buyers or sellers are driving the auction can help identify potential exhaustion points and support institutional-level entry timing.",
    "Volume spread analysis focuses on the relationship between price spread, volume, and closing price of individual bars. When high volume produces very little price movement, it suggests that opposing orders are absorbing the move, which often signals an impending reversal or pause. Conversely, wide bars on high volume confirm true momentum and institutional participation. Analyzing volume helps validate whether a breakout is genuine or a trap designed to capture retail liquidity.",
    "Fibonacci retracement levels are mathematical reference points derived from natural sequences that many traders use to anticipate support and resistance during pullbacks. Common retracement levels include 38.2 percent, 50 percent, and 61.8 percent. While these levels do not cause price to react on their own, they often align with previous structure, supply and demand zones, or moving averages, creating confluence that traders use to establish favorable risk-reward entries.",
    "Moving averages are among the most popular trend-following tools because they smooth out price fluctuations to reveal the underlying direction. Traders frequently look at short-term averages like the 20 EMA to gauge immediate momentum, while longer averages like the 50 or 200 SMA highlight long-term trends. A moving average does not predict the future, but it offers a dynamic framework for identifying trend bias, potential pullback areas, and momentum shifts.",
    "Momentum divergence occurs when price makes a new extreme, such as a higher high or lower low, while an oscillator like the RSI or MACD fails to confirm it. A bearish divergence suggests that upward momentum is fading despite rising prices, while a bullish divergence indicates weakening selling pressure. Although divergence warns of potential exhaustion, traders typically wait for a confirmed price break before entering, as strong trends can sustain divergences for long periods.",
    "Volatility squeezes occur during extended periods of market consolidation where price compression reaches extreme levels. Bollinger Bands contracting inside Keltner Channels is a common way to visualize this compression. Because low-volatility environments are almost always followed by explosive volatility expansion, identifying a squeeze allows traders to prepare for sharp breakout moves, provided they maintain disciplined entry confirmations and risk boundaries.",
    "Trailing stop-loss orders allow traders to protect accumulated profits while giving winning positions room to capture large market trends. By adjusting the stop level behind key swing points, moving averages, or volatility metrics like the Average True Range, a trader ensures that sudden reversals do not erase open gains. However, setting a trailing stop too tight risks getting stopped out by normal market noise before the larger trend develops.",
    "Fixed fractional position sizing is a risk management method where a trader risks the exact same percentage of their account balance on every trade, such as one or two percent. As the account balance grows, the monetary risk per trade increases proportionally, and when drawdowns occur, the risk decreases automatically. This systematic approach shields the account from catastrophic ruin during extended losing streaks while facilitating sustainable long-term compounding.",
    "Mental capital is just as important as financial capital for active market participants. Experiencing a series of frustrating losses, technical glitches, or missed setups can drain cognitive energy and lead to decision fatigue. When mental capital is exhausted, traders are far more prone to impulsive entries and emotional mistakes. Recognizing psychological fatigue and stepping away from the charts is often the most profitable decision a trader can make on difficult days."
]

@app.route('/')
def home():
    return "Discord Auto-Poster Bot is running 24/7!"

def send_messages():
    print("[+] Background Auto-Poster Started!")
    time.sleep(3)
    
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": USER_TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    available_paragraphs = paragraphs.copy()
    random.shuffle(available_paragraphs)
    msg_count = 0

    while True:
        try:
            if not available_paragraphs:
                available_paragraphs = paragraphs.copy()
                random.shuffle(available_paragraphs)
                print("[INFO] Sabhi paragraphs send ho chuke hain. Reshuffled.")

            message = available_paragraphs.pop()
            data = {"content": message}

            response = requests.post(url, headers=headers, json=data)

            if response.status_code in (200, 201):
                msg_count += 1
                print(f"[{time.strftime('%H:%M:%S')}] Message #{msg_count} Sent Successfully!")
                time.sleep(335)

            elif response.status_code == 429:
                retry_after = response.json().get("retry_after", 100)
                print(f"[RATE LIMIT] Slowmode active. Waiting for {retry_after} seconds...")
                time.sleep(retry_after + 2)

            else:
                print(f"[ERROR] Failed to send. Status Code: {response.status_code}, Response: {response.text}")
                time.sleep(10)

        except Exception as e:
            print(f"[EXCEPTION] Error occurred: {e}")
            time.sleep(10)

# Background Thread start karenge taaki Flask server ke sath loop bhi chale
def start_background_task():
    t = threading.Thread(target=send_messages, daemon=True)
    t.start()

start_background_task()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
