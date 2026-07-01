import time
from config import NEWS_API_KEY
from services.news import fetch_news
from services.ai import risk_score
from services.alert import send_alert

seen = set()

print("🚀 Bot started...")

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

            print(f"{title} | {score}")

            if score >= 50:
                send_alert(f"🚨 ALERT ({score}/100)\n{title}")

        time.sleep(60)

    except Exception as e:
        print("error:", e)
        time.sleep(10)
