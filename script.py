import os

try:
    print(f'EMAIL: {os.environ["EMAIL_ADDRESS"]}')
    print(f'PASSWORD: {os.environ["EMAIL_PW"]}')
except KeyError:
    print('Not Found')
