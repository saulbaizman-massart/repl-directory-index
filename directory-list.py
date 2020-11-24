#!/opt/virtualenvs/python3/bin/python
'''
DO NOT DELETE THIS FILE.

This program prints a directory with links to HTML, PDF, and text files.

To create the directory, press Command + Shift + S. In the Terminal window, enter:

$ python directory-list.py

WARNING: this will over-write index.html.
'''

import os

def is_valid_file_type (filename ) :

  valid_file_types = [ 'pdf', 'html', 'txt' ]

  _, extension = os.path.splitext(filename)

  if extension.lower()[1:] in valid_file_types:
    return True
  else:
    return False

def format_link ( url, target ) :
  return '<li><a href="/%s" target="_blank">%s</a></li>' % ( url, target )

repl_owner = os.environ['REPL_OWNER']
repl_name = os.environ['REPL_SLUG'].replace('-',' ')

folders = os.listdir('.')
'''
All repls can have a file named ".env" which stores key/value pairs that can be easily read by Python. More details are here:
https://docs.repl.it/repls/secret-keys
'''
header='''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>%s: %s</title>
  </head>
  <body>
    <h1>%s: %s</h1>
''' % (repl_owner, repl_name, repl_owner, repl_name )

content = []

content.append('<ul>')
for folder in folders:
  if os.path.isdir(folder): # is it a folder?
    content.append('<li>%s</li>' % folder )
    content.append('<ul>')
    files = os.listdir(folder)
    #print(files)
    for file in files:
      if os.path.isfile(os.path.join(folder,file)): # is it a file?
        # is it a pdf or html file?
        if is_valid_file_type (file):
          content.append( format_link ( os.path.join(folder,file), file ) )
      if os.path.isdir(os.path.join(folder,file)):
        subfolder_files = os.listdir(os.path.join(folder,file))
        for subfolder_file in subfolder_files:
        # is it a pdf or html file?
          if is_valid_file_type (subfolder_file):
            content.append( format_link ( os.path.join(folder,file,subfolder_file), subfolder_file ) )
    
    content.append('</ul>')
  
content.append('</ul>')

footer='''
  </body>
</html>
'''

# write to the file
index = open("index.html", "w")
index.write(header)
index.write(''.join(content))
index.write(footer)
index.close()
