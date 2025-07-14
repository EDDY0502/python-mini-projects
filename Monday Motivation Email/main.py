import smtplib                       # To send emails
import datetime as dt               # To get the day
import random                       # To choose a random quote

# Email credentials
my_email = "test.hiren5@gmail.com"
password = "ybhl zsfc zmfn vkys"
to_send = "test.hiren5@yahoo.com"

# Get the current day
now = dt.datetime.now()
weekday = now.weekday()             # Monday = 0

# Only send email if it's Monday
if weekday == 0:
    # Read all quotes from file
    with open("Birthday Wisher (Day 32) start/quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)  # Pick one random quote

    print(quote)  # Optional: see the quote in terminal

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # ✅ Add port 587
        connection.starttls()                                # Secure connection
        connection.login(user=my_email, password=password)   # Login to email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_send,
            msg=f"Subject:Monday Motivation\n\n{quote}"      # ✅ Use f-string to include the quote
        )
















'''import smtplib

my_email="test.hiren5@gmail.com"
password="ybhl zsfc zmfn vkys"
to_send="test.hiren5@yahoo.com" 

with smtplib.SMTP("smtp.gmail.com", 587) as connection: #Port 587 is the official port used for sending emails securely |connect to smpt gmail server|hotmail->smtp.live.com, yahoo->smtp.mail.yahoo.com
    connection.starttls()    #tls->Transport Layer Security| secure our way to connect to server
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to_send, 
                        msg="Subject:this is a mail\n\nThis is body of my email")'''


'''import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day

print (day)

date_of_birth= dt.datetime(year=2004,month=2,day=5)
print(date_of_birth)'''