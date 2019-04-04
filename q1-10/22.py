
import os
import argparse
import ftplib
import getpass 

LOCAL_FTP_SERVER = 'localhost'
LOCAL_FILE = 'file1.txt'

def ftp_upload(ftp_server, file_name):
    print ("Connecting to FTP server: %s" %ftp_server)
    ftp = ftplib.FTP(ftp_server)
    ext = os.path.splitext(file_name)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file_name, open(file_name))
    else:
        ftp.storbinary("STOR " + file_name, open(file_name, "rb"), 1024)
    print ("Uploaded file: %s" %file_name)


if __name__ == '__main__':
    ftp_server='192.168.43.218'
    ftp_upload(ftp_server,'file1.txt')

