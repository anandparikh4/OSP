from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def send_email(subject,text,send_address):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('noreplyospgrp8@gmail.com', 'osp_password')
    message = MIMEMultipart()
    message['Subject'] = subject
    message.attach(MIMEText(text))
    smtp.sendmail(from_addr='noreplyospgrp8@gmail.com',to_addrs=send_address, msg=message.as_string())
    smtp.quit()