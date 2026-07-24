import datetime
import pandas # type: ignore
import random
import smtplib

MY_EMAIL = "test.hiren5@gmail.com"
MY_PASSWORD = "dwof smar oyrd hpam"  # Gmail App Password

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Dictionary with (month, day) as key
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

# Check if today matches any birthday
if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]

    # Pick random letter and replace [NAME]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, encoding="utf-8") as letter_file:
        content = letter_file.read().replace("[NAME]", person["name"])

    # Clean email
    recipient = str(person["email"]).strip().replace("\u200b", "")

    # Prepare message
    msg = f"Subject: Happy Birthday!\n\n{content}"

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, recipient, msg)

    print(f"✅ Birthday email sent to {recipient}")
else:
    print("No birthdays today.")
