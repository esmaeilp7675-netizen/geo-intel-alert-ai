import time
from config import NEWS_API_KEY
from services.news import fetch_news
from services.ai import risk_score
from services.alert import send_alert

seen_articles = set()

print("🚀 Geo Intel AI System Started...")

while True:
    try:
        data = fetch_news(NEWS_API_KEY)

        articles = data.get("articles", [])

        for article in articles:
            title = article.get("title")

            if not title:
                continue

            if title in seen_articles:
                continue

            seen_articles.add(title)

            score = risk_score(title)

            print(f"Checked: {title} | Risk: {score}")

            if score >= 50:
                send_alert(
                    f"🚨 GEO INTEL ALERT ({score}/100)\n\n{title}"
                )

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
