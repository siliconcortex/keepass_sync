from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.


drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'passwords_test.kdbx'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
# file1.SetContentString('Hello World!') # Set content of the file from given string.

print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
folderpath = os.path.dirname(os.path.realpath(__file__)).replace(__file__, '') + '/'



file1.SetContentFile(folderpath + 'Database_test.kdbx') # Set content of the file from given string.

file1.Upload()
print('Done.')