import time
import threading
from flask import Flask
from config import NEWS_API_KEY
from services.news import fetch_news
from services.ai import risk_score
from services.alert import send_alert

app = Flask(__name__)

seen = set()

def bot_loop():
    while True:
        try:
            data = fetch_news(NEWS_API_KEY)
            articles = data.get("articles", [])

            for a in articles:
                title = a.get("title")

                if not title or title in seen:
                    continue

                seen.add(title)

                score = risk_score(title)

                print(f"Checked: {title} | Risk: {score}")

                if score >= 50:
                    send_alert(f"🚨 ALERT ({score}) - {title}")

            time.sleep(60)

        except Exception as e:
            print("Error:", e)
            time.sleep(10)


@app.route("/")
def home():
    return {
        "status": "ok",
        "service": "Geo Intel AI",
        "mode": "web + worker combined"
    }


if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
