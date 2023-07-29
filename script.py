import smtplib
import ssl
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(send_to, msg):
    'Establishes a secure connection to an email service and sends an email'
    port = 465  # ssl port

    # create a secure SSL context
    context = ssl.create_default_context()

    # connect to smtp service and send an email
    print(' > Connecting to email service ... ')
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        print(' > Logging in ... ')
        server.login(FROM_ADDR, PW)
        print(' > Sending message ... ')
        server.sendmail(FROM_ADDR, send_to, msg)


def build_message():
    'Builds an email message'
    # message data
    to_addr = input('Who would you like to send an email to? > ')
    message = """\
    Subject: Testing...

    Hello, world!

    This message is sent from some Python code.
    - Jaxon"""
    return to_addr, message


# !----------------------------------------------
if __name__ == '__main__':
    # pull email address and password from environment variables
    # mine are set in my virtual environment
    try:
        FROM_ADDR = os.environ['EMAIL_ADDRESS']
        PW = os.environ['EMAIL_PW']
    except KeyError:
        print('Email address and password not found.')
        sys.exit()

    try:
        msg = build_message()
        send_mail(*msg)
    except Exception as e:
        print(f'Sorry, something went wrong: {e}')
        sys.exit()
    else:
        print('Your email has been sent!')
