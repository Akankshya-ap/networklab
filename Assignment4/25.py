import os

mail = input("Enter the email address : ")
mail = mail.split('@')
if len(mail) == 1:
        mail = mail[0]
else:
        mail = mail[1]

os.system("host "+mail)
