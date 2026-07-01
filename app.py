import time
from config import NEWS_API_KEY
from services.news import fetch_news
from services.ai import risk_score
from services.alert import send_alert

seen_articles = set()

print("🚀 Geo Intel AI System Started...")


        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Geo Intel AI is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
