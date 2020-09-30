import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Moneygram'
email['to'] = 'sneha.c796@gmail.com'
email['subject'] = 'You have Won rs.1000!!'

email.set_content(html.substitute({'name':'abc'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()  
	smtp.login('sneha.c796@gmail.com','$nEh@0c7')
	smtp.send_message(email)
	print('Logged in Successfully!!')
