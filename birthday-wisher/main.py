import datetime
import pandas # type: ignore
import random
import smtplib

MY_EMAIL = "test.hiren5@gmail.com" # Your email address
MY_PASSWORD = "dwof smar oyrd hpam"  # Gmail App Password

today = datetime.datetime.now() # Get current date
today_tuple = (today.month, today.day) # (month, day)

# Read birthdays.csv
data = pandas.read_csv("birthdays.csv") # type: ignore

# Dictionary with (month, day) as key
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()} # type: ignore

# Check if today matches any birthday
if today_tuple in birthdays_dict: # If birthday today
    person = birthdays_dict[today_tuple] # Get birthday person

    # Pick random letter and replace [NAME]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt" # Random letter file
    with open(file_path, encoding="utf-8") as letter_file: # Open letter file
        content = letter_file.read().replace("[NAME]", person["name"]) # Replace [NAME] with actual name

    # Clean email
    recipient = str(person["email"]).strip().replace("\u200b", "") # Clean email address

    # Prepare message
    msg = f"Subject: Happy Birthday!\n\n{content}" # Email message

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection: # Connect to SMTP server
        connection.starttls() # Start TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD) # Login to email account
        connection.sendmail(MY_EMAIL, recipient, msg) # Send email

    print(f"✅ Birthday email sent to {recipient}") # Confirmation message
else: 
    print("No birthdays today.") # No birthdays today