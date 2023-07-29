import smtplib
import ssl
import os
import sys

port = 465  # For SSL

# pull email address and password from environment variables
# mine are set in my virtual environment
try:
    from_addr = os.environ['EMAIL_ADDRESS']
    pw = os.environ['EMAIL_PW']
except KeyError:
    print('Email address and password not found.')
    sys.exit()

# message data
receiver_email = input('Who would you like to send an email to? > ')
message = """\
Subject: Testing...

This message is sent from Python.
 - Jaxon"""

# create a secure SSL context
context = ssl.create_default_context()

# connect to smtp service and send an email
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(from_addr, pw)
    server.sendmail(from_addr, receiver_email, message)
