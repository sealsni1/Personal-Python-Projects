import os


#file_path = '/Users/nickseals/Downloads/.zip'

#print(file_path)

#if os.path.isfile(file_path):
    #os.remove(file_path)
    #print('File has been successfully deleted')

#else:
    #print('This file does NOT exists')


directory_path = '/Users/nickseals/Downloads/'

# List all files in the directory
file_list = os.listdir(directory_path)

for filename in file_list:

    #if filename.startswith('Ch') or filename.endswith(".xlsx"):
    if filename.endswith('.zip'):

        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):

            os.remove(file_path)
            print(f'File {filename} has been successfully deleted')

print('Deletion process completed.')
