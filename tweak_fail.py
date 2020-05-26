import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "05afa952a6d1be"
host_pass = "c982006177d8a8"
guest_address = "akanksha.6698@gmail.com"
subject = " [Alert] failure of tweak.py"
content = '''Hey, 
				After Developer's commit error while re-training model we are here with an update.Again the training is going to be proceeded.
			THANK YOU
            CI/CD team'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.mailtrap.io', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Mail Sent...')
