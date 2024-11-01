import smtplib

def send_email():
    my_email = "leandro.lpalermo@gmail.com"
    password = "ybnx lgkv kbzn clon"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Hello\n\nThis is the body of my email."
        )


import datetime as dt
now = dt.datetime.now()
print(now)
print(now.year)
print(now.weekday())
print(now.isoweekday())

day_of_birth = dt.datetime(year=1986, month=4, day=2)
print(day_of_birth)
