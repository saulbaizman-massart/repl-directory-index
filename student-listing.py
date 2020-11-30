#!/opt/virtualenvs/python3/bin/python

'''
To run this program, press Command + Shift + S. In the Terminal window enter the following command:

$ python student-listing.py

To update to the latest version:

$ wget -O student-listing.py https://raw.githubusercontent.com/saulbaizman-massart/repl-directory-index/master/student-listing.py
'''

def format_link ( url, target ) :
    """Format a link."""
    return '<a href="https://%s" target="_blank" rel="noopener">%s</a>' % ( url, target )

name_map = {}
name_map['Cj'] = 'cjray22' # "Cj" is half-lowercased so that the name appears in the correct alphabetical order
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
repl_map['cjray22'] = ['homework','final-project','client-website',]
repl_map['ceallard'] = ['Homework','Final-Project','Client-Website',]
repl_map['DanielGrieco'] = ['homework','Final-Project','Client-Website',]
repl_map['EmSpaulding0707'] = ['homework','Final-Project','Client-Websitehtml',]
repl_map['EmilyHCC'] = ['Homework','Final-Project','Client-Website',]
repl_map['jponeillsantiag'] = ['homework','Final-Project','client-website',]
repl_map['kadbril'] = ['homework','Final-Project','Client-Website',]
repl_map['KerryBlanchard'] = ['homework','Final-Project','Client-Website',]
repl_map['Motsuki1120'] = ['homework','final-project','client-website',]
repl_map['MeghanYip'] = ['homework','FinalProject','client-website',]
repl_map['omatheson99'] = ['Homework','Final-Project',]
repl_map['tanyaandreeva'] = ['Homework','Final-Project','Client-Website',]

header='''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>student directory &mdash; fa20</title>
    <style type="text/css">
    * { font-family: Helvetica, Arial, sans-serif }
    body { margin: 50px }
    ul ul { margin-bottom: 20px }
    li { line-height: 1.55em }
    a { text-decoration: none; color: red }
    a:hover, a:focus { background-color: rgba(250,0,0,.1) }
    body > div.grid_parent > li { list-style-type: none; padding-left: 0; font-size: 2rem; font-weight: bold }
    body > div.grid_parent > li > ul { margin-top:0; padding-left: 0 }
    body > div.grid_parent > li > ul > li { font-size: 1rem; font-weight: normal }
    body > div.grid_parent { display: grid; grid-template-columns: repeat(4,1fr); grid-template-rows: repeat(3,1fr); grid-auto-flow: column }
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

content.append('<div class="grid_parent">')

# loop through students
for student in sorted (name_map.keys()):
    real_name = student.lower()
    repl_username = name_map[student]
    content.append ( '<li>%s' % format_link ( 'repl.it/@%s' % repl_username, real_name ) )
    content.append('<ul>')

    # loop through each student's list of repls
    for repl in repl_map[repl_username]:
        repl_clean = repl.lower().replace('-',' ')
        content.append ( '<li>%s: %s | %s</li>' % ( repl_clean, format_link('repl.it/@%s/%s/' % ( repl_username, repl ) , 'repl'), format_link('%s.%s.repl.co' % ( repl, repl_username ), 'website') ) )

    content.append('</ul>')
    content.append('</li>')

content.append('</div>')

# write to the file
index = open("index.html", "w")
index.write(header)
index.write("\n".join(content))
index.write(footer)
index.close()
