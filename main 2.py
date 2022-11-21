import pandas
import random
from datetime import datetime
import smtplib

MY_EMAIL = "fly@angelfly.xyz"
MY_PASSWORD = "Surf.1993"
receiver = "gabriel@grupofly.com.br"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()

        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("mail.angelfly.xyz:587") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=str(birthday_person["email"]),
            msg=f"Subject:Happy Birthday to: {birthday_person['name']}\n\n{contents}"
        )
