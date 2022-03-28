from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from decouple import config


def send_email(subject,text,receive_address):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    sender_mail = config('USERNAME')
    sender_password = config('PASSWORD')
    smtp.login(sender_mail, sender_password)
    message = MIMEMultipart()
    message['Subject'] = subject
    message.attach(MIMEText(text))
    smtp.sendmail(from_addr='noreplyospgrp8@gmail.com',to_addrs=receive_address, msg=message.as_string())
    smtp.quit()