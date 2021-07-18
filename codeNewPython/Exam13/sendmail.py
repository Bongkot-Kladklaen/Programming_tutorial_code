import smtplib
sender = 'from@email.com'
pwd = 'xxxx'
receivers = 'to@email.com'
message = """From: sender <from@gmail.com> 
To: Receiver <to@email.com>
Subject: SMTP send Email
Hello python send Email."""

try :
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pwd)
    server.sendmail(sender, receivers , message)
    server.quit()
    print ("Successfully sent email")
except SMTPException:
    print ("Error: unable to send email")

 #Less secure app access
