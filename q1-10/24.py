
import argparse
import getpass
import poplib

GOOGLE_POP3_SERVER = 'pop.googlemail.com'

def download_email(username): 
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, '995') 
    mailbox.user(username)
    password = getpass.getpass(prompt="Enter your Google password: ") 
    mailbox.pass_(password) 
    num_messages = len(mailbox.list()[1])
    print ("Total emails: %s" %num_messages)
    print ("Getting last message")
    for msg in mailbox.retr(num_messages)[1]:
        print (msg)
    mailbox.quit()

if __name__ == '__main__':
  
    username = 'ayesha199718@gmail.com'
    download_email(username)
