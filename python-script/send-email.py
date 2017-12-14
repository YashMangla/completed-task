import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromadd = 'Sender E-Mail'
toadd = 'Receiver E-mail'
msg = MIMEMultipart()
msg['From'] = fromadd
msg['To'] = toadd
msg['Subject'] = 'Test Mail'

body = "Hello Everyone ! Tell me something about your day?"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromadd, "Sender Pwd")
text = msg.as_string()
server.sendmail(fromadd, toadd, text)
server.quit()