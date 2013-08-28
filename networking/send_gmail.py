#!/usr/bin/python
import smtplib
from email.Message import Message
from time import sleep

smtpserver='smtp.gmail.com'
username='babyanuo@gmail.com'
password='********'
from_addr='babyanuo@gmail.com'
to_addr='jean.zhang.cn@gmail.com'
cc_addr='jean.zhang@outlook.com'

message=Message()
message['Subject']='Mail Subject'
message['From']=from_addr
message['To']=to_addr
message['Cc']=cc_addr
message.set_payload('mail content')
msg=message.as_string()

sm=smtplib.SMTP(smtpserver,port=587,timeout=20)
sm.set_debuglevel(1)
sm.ehlo()
sm.starttls()
sm.ehlo()
sm.login(username,password)
sm.sendmail(from_addr,to_addr,msg)
sleep(5)
sm.quit()
