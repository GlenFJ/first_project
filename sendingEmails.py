import  smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='Glen Francis Joseph'
email['to'] ='glen4u@gmail.com'
email['subject']='Glen is master in Python programming'

email.set_content('I am a python Master')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('glen4u@gmail.om','Anthony45')
    smtp.send_message(email)
    print('Email sent sucessfuuly!')
