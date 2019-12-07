from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

def delete(FILENAME_DELETE):
	# Auto-iterate through all files that matches this query
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for file1 in file_list:
	  print('title: %s, id: %s' % (file1['title'], file1['id']))
	  #if file has name #NAME, delete the file.
	  if file1['title'] == FILENAME_DELETE:
	  	file1.Trash()
		# Initialize GoogleDriveFile instance with file id.

	# file1.Trash()  # Move file to trash.
	# file1.UnTrash()  # Move file out of trash.
	# file1.Delete()  # Permanently delete the file.

def upload(FILENAME_UPLOAD):

	file1 = drive.CreateFile({'title': FILENAME_UPLOAD})  # Create GoogleDriveFile instance with title 'Hello.txt'.
	# file1.SetContentString('Hello World!') # Set content of the file from given string.

	print(__file__)
	print(os.path.realpath(__file__))
	print(os.path.dirname(os.path.realpath(__file__)))
	folderpath = os.path.dirname(os.path.realpath(__file__)).replace(__file__, '') + '/'

	file1.SetContentFile(folderpath + FILENAME_UPLOAD) # Set content of the file from given string.
	delete(FILENAME_UPLOAD)
	file1.Upload()
	print('Done.')

upload('Database.kdbx')

