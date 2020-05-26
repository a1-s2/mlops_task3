# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "sabhi8226@gmail.com"
# Receivers email
rec_email = "sabhi8226@gmail.com"

message = (""" The Accuracy Of uR MoDel is GoOod nOw u caN ProceeD FurThur ! """)

# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("sabhi8226@gmail.com", "Abhi12345@8269406717")
print("Login Success!")
# Send Email
server.sendmail("abhi saini", "sabhi8226@gmail,com", message)
print(f"Email has been sent successfully to {rec_email}")
