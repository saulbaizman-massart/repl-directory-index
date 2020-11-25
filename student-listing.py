#!/opt/virtualenvs/python3/bin/python

'''
To run, press Command + Shift + S. In the Terminal window enter the following command:

$ python student-listing.py

To update to the latest version:

$ wget -O student-listing.py https://raw.githubusercontent.com/saulbaizman-massart/repl-directory-index/master/student-listing.py
'''

'''
object structure:
name (string)
username (string)
repls (list)
+ repl path (string)
+ repl url (string, computable based on repl path and username)

'''

'''
class Student:
    def __init__ (self, real_name, repl_username):
        self.real_name = real_name
        self.repl_username = repl_username
        self.repls = [] # empty list
    
    def add_repl (self, repl_path):
        self.repls.append (repl_path) # add path to list

'''

def format_link ( url, target ) :
    return '<a href="https://%s" target="_blank">%s</a>' % ( url, target )

name_map = {}
name_map['Cj'] = 'cjray22'
name_map['Chloe'] = 'ceallard'
name_map['Daniel'] = 'DanielGrieco'
name_map['Emma'] = 'EmSpaulding0707'
name_map['Emily'] = 'EmilyHCC'
name_map['Jean Paul'] = 'jponeillsantiag'
name_map['Kade'] = 'kadbril'
name_map['Kerry'] = 'KerryBlanchard'
name_map['Mao'] = 'Motsuki1120'
name_map['Meghan'] = 'MeghanYip'
name_map['Olivia'] = 'omatheson99'
name_map['Tanya'] = 'tanyaandreeva'

repl_map = {}
repl_map['cjray22'] = ['homework','final-project']
repl_map['ceallard'] = ['Homework','Final-Project']
repl_map['DanielGrieco'] = ['homework','Final-Project']
repl_map['EmSpaulding0707'] = ['homework','Final-Project']
repl_map['EmilyHCC'] = ['Homework','Final-Project']
repl_map['jponeillsantiag'] = ['homework','Final-Project']
repl_map['kadbril'] = ['homework','Final-Project']
repl_map['KerryBlanchard'] = ['homework','Final-Project']
repl_map['Motsuki1120'] = ['homework','final-project']
repl_map['MeghanYip'] = ['homework','FinalProject']
repl_map['omatheson99'] = ['Homework','Final-Project']
repl_map['tanyaandreeva'] = ['Homework','Final-Project']

header='''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>student directory &mdash; fa20</title>
    <style type="text/css">
    * { font-family: Helvetica, Arial, sans-serif }
    ul > ul { margin-bottom: 15px }
    li { line-height: 1.55em }
    </style>
  </head>
  <body>
    <h1>student directory &mdash; fa20</h1>
'''

footer='''
  </body>
</html>
'''
content = []

content.append('<ul>')

for student in sorted (name_map.keys()):
    real_name = student.lower()
    repl_username = name_map[student]
    content.append ( '<li>' )
    content.append ( format_link ( 'repl.it/@%s' % repl_username, real_name ) )
    content.append ( '</li>' )
    content.append ("\n")
    content.append('<ul>')
    for repl in repl_map[repl_username]:
        content.append ( '<li>' )
        content.append ( '%s: %s | %s' % ( repl, format_link('repl.it/@%s/%s/' % ( repl_username, repl ) ,'repl'), format_link('%s.%s.repl.co' % ( repl, repl_username ),'website') ) )
        content.append ( '</li>' )
        content.append ("\n")

    content.append('</ul>')
    content.append('</li>')

content.append('</ul>')

# print ( ''.join(content) )

# write to the file

index = open("index.html", "w")
index.write(header)
index.write(''.join(content))
index.write(footer)
index.close()
