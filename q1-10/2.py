from zipfile import ZipFile
import os

for root, dirs, files in os.walk("/home/administrator/Desktop/115cs0231/assignment4/use"):  
        file_paths = []
        for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath) 

with ZipFile('new_files.zip','w') as zip:
        for file in file_paths:
                zip.write(file)
  
print('All files zipped successfully!')
#newZip.write('use/spam.txt', compress_type=zipfile.ZIP_DEFLATED)
