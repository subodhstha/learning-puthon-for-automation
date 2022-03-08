
import smtplib
from email.message import EmailMessage

EMAIL_ADD = 'pythonautomationtest1@gmail.com'
EMAIL_PASS = '@&dj12j23'

msg = EmailMessage()
msg['Subject'] = 'grab dinner'
msg['From'] = EMAIL_ADD
msg['To'] = 'pdsc.nepal@gmail.com'
msg.set_content('whats cooking?')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADD ,EMAIL_PASS)
    smtp.send_message(msg)
