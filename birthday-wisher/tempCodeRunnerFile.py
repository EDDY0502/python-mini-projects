import datetime
import pandas
import random
import smtplib

MY_EMAIL = "test.hiren5@gmail.com"
MY_PASSWORD = "chandwani"  # ⚠️ Use App Password instead

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Dictionary with (month, day) as key
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

# Check if today matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Pick random letter template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        context = letter_file.read()
        context = context.replace("[NAME]", birthday_person["name"])

    # Format email properly
    msg = f"Subject: Happy Birthday!\nTo: {birthday_person['email']}\nFrom: {MY_EMAIL}\n\n{context}"

    # Send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=msg
        )
