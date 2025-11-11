thonimport random

def get_proxy():
    proxies = [
        "http://proxy1.example.com",
        "http://proxy2.example.com",
        "http://proxy3.example.com"
    ]
    return {"http": random.choice(proxies), "https": random.choice(proxies)}

def save_data(data, filename):
    with open(f"whop-com-leaderboards-scraper/data/{filename}", 'w') as f:
        json.dump(data, f, indent=4)