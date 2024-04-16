#!/usr/bin/python3
import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import sys

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()

server.login(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))

msg = MIMEMultipart()
msg['from'] = str(os.environ.get("FROM_EMAIL"))
msg['to'] = str(os.environ.get("TO_EMAIL"))
msg['subject'] = sys.argv[1]

with open('message.txt', 'r') as file:
    msg = file.read()

msg.attach(MIMEText(msg, 'plain'))
image_name = 'image.jpg'
attachment = open(image_name, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={image_name}')
msg.attach(p)
text = msg.as_string()
server.sendmail(os.environ.get("EMAIL"), os.environ.get("TO_EMAIL"), text)

attachment.close()
server.quit()
