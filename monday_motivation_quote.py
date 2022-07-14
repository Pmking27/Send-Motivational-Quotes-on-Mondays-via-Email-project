import smtplib
import datetime as dt
import random


my_email="Your Email"
my_password="Your Email Password Or If you using Gmail Then App Key"

receiver_emails=["Enter here receiver emails"]

quote=""
with open("quotes.txt","r") as day_quote: 
    quote=day_quote.readlines()
rand_quote=random.choice(quote)
print(rand_quote)
data=dt.datetime.now()
day_of_week=data.weekday()
with smtplib.SMTP("smtp.gmail.com") as connection: #<--here enter your smtp host address
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    if day_of_week==0:
        for i in range(len(receiver_emails)):
            connection.sendmail(from_addr=my_email,to_addrs=receiver_emails[i],msg=f"Subject:Monday Motivation Quote \n\n{rand_quote}")
