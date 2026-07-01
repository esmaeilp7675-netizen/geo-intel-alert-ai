import requests

def fetch_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=10&apiKey={api_key}"
    return requests.get(url).json()
