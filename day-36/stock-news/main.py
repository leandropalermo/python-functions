import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "VJKQ07QMFTTIFJCY"
NEWS_API_KEY = "2a2b0b03f5bf4cda9e36997f3e05f5b3"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def calculate_percentage(actual_value: float, previous_value: float) -> float:
    return ((actual_value / previous_value) - 1) * 100


def fetch_news():
    news_param = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    response.raise_for_status()

    return [article for article in response.json()['articles']][0:3]


def calculate_stock_price_movement(stock_name: str):
    stock_api_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_name,
        "apikey": STOCK_API_KEY
    }

    response = requests.get(url=STOCK_ENDPOINT, params=stock_api_params)
    response.raise_for_status()
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]
    last_closed_day = data_list[0]
    last_closed_day_price = last_closed_day["4. close"]

    day_before_last_closed_day = data_list[1]
    day_before_last_closed_day_price = day_before_last_closed_day["4. close"]

    percentage_difference = calculate_percentage(float(last_closed_day_price), float(day_before_last_closed_day_price))
    stock_signal = "🔺"
    if percentage_difference < 0:
        stock_signal = "🔻"

    articles = fetch_news()
    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}\n" for article in articles]

    for article in formatted_articles:
        print(f"{stock_name}: {stock_signal}{round(percentage_difference, 2)}%")
        print(article)


calculate_stock_price_movement(STOCK_NAME)

