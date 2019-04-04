
import argparse
import getpass
import poplib
import os
import re
import sys
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
def send_email(sender, recipient):
    msg = MIMEMultipart()
    msg['Subject'] = 'Python Emaill Test'
    msg['To'] = recipient
    msg['From'] = sender
    subject = 'Python email Test'
    message = 'Images attached.'
    # attach imgae files
    files = os.listdir(os.getcwd())
    gifsearch = re.compile(".gif", re.IGNORECASE)
    files = filter(gifsearch.search, files)
    for filename in files:
        path = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(path):
            continue
        img = MIMEImage(open(path, 'rb').read(), _subtype="gif")
        img.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(img)
 
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    
    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    password = getpass.getpass(prompt="Enter your Google password: ") 
    session.login(sender, password)
    session.sendmail(sender, recipient, msg.as_string())
    print ("Email sent.")

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Send')
    parser.add_argument('--sender', action="store", dest="sender")
    parser.add_argument('--recipient', action="store", dest="recipient")
    given_args = parser.parse_args()
    send_email(given_args.sender, given_args.recipient)
