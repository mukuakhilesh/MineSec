import smtplib
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
receiver = ('akhibiada007@gmail.com','ashish.aryan099@gmail.com','pp981057@gmail.com','mklwra@gmail.com')
sub="alert"
co=True
ch4=False
temp=True
msg=""
if co:
 msg+="carbon monoxide "
if ch4:
 msg+="methane"
if temp:
 msg+="temp"
msg+=" exceeded"
msg=msg+" on alert"
sender = 'ashish.aryan099@gmail.com'

msg="""From:from ashish.aryan099@gmail.com
To:to akhi.biada007@gmail.com
Subject:%s

%s
"""%(sub,msg)
try:
	server.login('ashish.aryan099@gmail.com','8969675310')
        for id in receiver:
	 print id
	 server.sendmail('ashish.aryan099@gmail.com',str(id),msg)
	server.quit()
	print ("message sent")
except SMTPException:
	print('mail not sent')

