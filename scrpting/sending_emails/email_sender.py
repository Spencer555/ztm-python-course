import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path
# smtp allows us to create an smtp server it the protocol of email just like http is for website
# smtp - simple mail transfer protocol 


# get html page and read text from am 
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Spencer Lewis'
email['to'] = 'lewisspencer555@gmail.com'
email['subject'] = 'testing 1 2'


email.set_content(html.substitute({'name':'spencer elvis'}), 'html')



with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()#an encryption mechnism to connect securely to the server
    smtp.login('spldevwebapps@gmail.com', 'enter your own password')
    smtp.send_message(email)
    print('all good boss!')