import random

def load_quotes(file_path="quotes.txt"):
    """从文件加载名言"""
    with open(file_path, "r", encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]
    return quotes

def get_random_quote(quotes):
    """随机返回一条名言"""
    return random.choice(quotes)

if __name__ == "__main__":
    quotes = load_quotes()
    print("💡 今日名言：")
    print(get_random_quote(quotes))
