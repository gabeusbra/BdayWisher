import smtplib
import datetime as dt
import random


my_email = "fly@angelfly.xyz"
password = "Surf.1993"
receiver = "gabriel@grupofly.com.br"

now = dt.datetime.now()
weekday = now.weekday()





def job():
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("mail.angelfly.xyz:587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=f"Subject:Monday Self Motivation :D \n\n{quote}"
        )



