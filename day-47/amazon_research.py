import smtplib

import requests
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

def send_email(price):
    my_email = "leandro.lpalermo@gmail.com"
    password = "ybnx lgkv kbzn clon"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Buy now, the price has dropped.\n\nThe price is ${price}"
        )

response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
price_result = soup.select(".aok-offscreen")
price = str(price_result).split('$')[1].split()[0]
price_as_float = float(price)

if price_as_float < 100:
    send_email(price_as_float)


print(price_as_float)