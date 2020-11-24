#!/opt/virtualenvs/python3/bin/python
'''
Saul says, DO NOT DELETE THIS FILE.

Print a directory with links to files.

To create the directory, press Command + Shift + S. In the Terminal window, enter:

$ chmod +x directory-list.py
$ ./directory-list.py > index.html

WARNING: this will over-write index.html.

'''

import os

folders = os.listdir('.')

print ('''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>final project</title>
  </head>
  <body>
    <h1>Final Project</h1>
''')

#print (folders)

print('<ul>')
for folder in folders:
  if os.path.isdir(folder): # is it a folder?
    print('<li>%s</li>' % folder )
    print('<ul>')
    files = os.listdir(folder)
    #print(files)
    for file in files:
      if os.path.isfile(os.path.join(folder,file)): # is it a file?
        print('<li><a href="/%s" target="_blank">%s</a></li>' % ( os.path.join(folder,file), file ) )
      if os.path.isdir(os.path.join(folder,file)):
        subfolder_files = os.listdir(os.path.join(folder,file))
        for subfolder_file in subfolder_files:
          print('<li><a href="/%s" target="_blank">%s</a></li>' % ( os.path.join(folder,file,subfolder_file), subfolder_file ) )
    
    print('</ul>')
  
print('</ul>')

print ('''
  </body>
</html>
''')
