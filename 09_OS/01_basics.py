import os

print('path:' ,os.getcwd()) #get working directory
print('full_path:', os.path.abspath(__file__)) #get absoulute path
print('Directory:', os.path.dirname (os.path.abspath(__file__))) #get the directory name of the current file
# print(os.listdir()) #list of all the files in the directory

for i in os.listdir():
    if os.path.isfile(i):
        print(f'{i} is a file')
    elif os.path.isdir(i):
     print(f'{i} is a directory')

last_load = '2026-01-14'
for i in os.listdir((os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data'))):
   if i.split(".")[0] > last_load: #splitting the data and csv in two diff part in list and then comparing the fist part of the list that is the date
      #logic to do processing
      print(f'Processing new file: {i}')
 