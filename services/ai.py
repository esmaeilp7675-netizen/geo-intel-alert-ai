def risk_score(text):
    keywords = {
        "war": 30,
        "attack": 25,
        "missile": 35,
        "strike": 25,
        "military": 20,
        "invasion": 40
    }

    score = 0
    text = text.lower()

    for k, v in keywords.items():
        if k in text:
            score += v

    return min(score, 100)
