from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From:')
password = input('password:')
to_addr = 'dabu570@163.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('这是测试邮件1......', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自STMP的问候......', 'utf-8').encode()

with smtplib.SMTP(smtp_server) as smtp:
    smtp.set_debuglevel(1)
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())
