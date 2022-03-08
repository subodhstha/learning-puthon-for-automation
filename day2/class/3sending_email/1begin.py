import os
import smtplib   #inbuilt

email_add = 'pythonautomationtest1@gmail.com'
passwd_pass  = '@&dj12j23'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login( email_add , passwd_pass)

    subject = 'hello'
    body = 'how you doing?'

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(email_add , 'pdsc.nepal@gmail.com', msg)
