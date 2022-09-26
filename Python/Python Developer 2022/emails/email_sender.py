import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #?similar to os.path

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'Gesban Data'
email['to'] = 'cayorch@gmail.com'
email['subject'] = 'You just won 1,000,000 USD!'

#email.set_content('I am a Python Master!')
email.set_content(html.substitute(name='Jorge'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gesbandata@gmail.com', 'ogomnjxzrridxepo')
    smtp.send_message(email)
    print('all good boss!')