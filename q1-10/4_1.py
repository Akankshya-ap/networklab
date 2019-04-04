import smtplib

from email.mime.text import MIMEText
textfile='1.txt'
fp = open(textfile, 'rb')

msg = MIMEText(fp.read())
fp.close()

me='ayesha.patra2@gmail.com'
you='ayesha.patra2@gmail.com'
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
