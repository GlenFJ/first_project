import  smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('forCustomEmail.html').read_text())
email=EmailMessage()
email['from']='Glen Francis Joseph'
email['to'] ='glen4u@gmail.com'
email['subject']='Glen is master in Python programming'

email.set_content(html.substitute({'name':'TinTin'}),html)

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('glen4u@gmail.om','Anthony45')
    smtp.send_message(email)
    print('Email sent sucessfuuly!')