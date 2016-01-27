#-*- coding: UTF-8 -*-
#
# def application(environ,start_responses):
#     start_responses('200 OK',[('content-Type','text/html')])
#     body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
#     return [body.encode('utf8')]
#
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'plutoliu@foxmail.com'
password = 'xczsspgcczacbhei'
to_addr = 'yfwsir@163.com'
smtp_server = 'smtp.qq.com'

#msg = MIMEText('hello, send by Python...鸟哥大傻逼', 'plain', 'utf-8') #纯文本邮件
msg = MIMEMultipart()
msg['From'] = _format_addr('Python大神 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#正文
msg.attach(MIMEText('鸟哥大黄人','plain','utf-8'))
with open('/Users/CNme/Desktop/login.png','rb') as f:
    mime = MIMEBase('image','png',filename='login.png')
    mime.add_header('Content-Disposition','attachment',filename='login.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

import smtplib
server = smtplib.SMTP(smtp_server,587)
server.starttls() # requires that you turn on encryption (start TLS) and authenticate before sending email.
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
