#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'tianxuean@gmail.com'
password = input('Password: ')# should input the application password, to get it on gmail.
to_addr = input('To: ')
#smtp_server = input('SMTP server: ')

smtp_server = 'smtp.gmail.com'
smtp_port = 587

server = smtplib.SMTP(smtp_server, smtp_port)



msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

#server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


if __name__ == '__main__':
    _format_addr('hello David')