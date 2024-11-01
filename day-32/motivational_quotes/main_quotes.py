import random
import smtplib
import datetime as dt

MY_EMAIL = "leandro.lpalermo@gmail.com"
MY_PASSWORD = "123455555"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 1:
    with open("main_quotes.py") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )