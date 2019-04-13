
import os
import argparse
import smtplib
import zipfile
import tempfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart    


sender='115cs0231@gmail.com'
recipient='115cs0221@gmail.com'


zf = tempfile.TemporaryFile(prefix='mail', suffix='.zip')
zip = zipfile.ZipFile(zf, 'w')
#print ("Zipping current dir: %s" %os.getcwd())
for file_name in os.listdir(os.getcwd()):
        zip.write(file_name)
zip.close()
zf.seek(0)

print ("Creating email message...")
email_msg = MIMEMultipart()
email_msg['Subject'] = 'File from path %s' %os.getcwd()
email_msg['To'] = ', '.join(recipient)
email_msg['From'] = sender
email_msg.preamble = 'Testing email from Python.\n'
msg = MIMEBase('application', 'zip')
msg.set_payload(zf.read())
encoders.encode_base64(msg)
msg.add_header('Content-Disposition', 'attachment', 
           filename=os.getcwd()[-1] + '.zip')
email_msg.attach(msg)
email_msg = email_msg.as_string()

print ("Sending email message...")
try:
        smtp = smtplib.SMTP('localhost')
        smtp.set_debuglevel(1)
        smtp.sendmail(sender, recipient, email_msg)
except Exception as e:
        print ("Error: %s" %str(e))
finally:
        smtp.close()


