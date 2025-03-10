import random, sys, requests, bs4
import openpyxl as xl
from openpyxl.styles import Font
import re
import shutil
from pathlib import Path

import smtplib
from email.message import EmailMessage

def main():
    website = 'https://moviesjoy.is/movie'
    res = requests.get(website)
    content = res.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    elems = soup.find_all('a')

    print(elems)

def SendEmail(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'pythonerrors404@gmail.com'
    msg['from'] = user
    password = 'xezzksakyhqxmsaa'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    SendEmail('9062354870@vtext.com', 'Start', 'Program has started')
    main()