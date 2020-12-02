#!/opt/virtualenvs/python3/bin/python
# -*- coding: utf-8 -*-

'''
To run this program, press Command + Shift + S. In the Terminal window enter the following command:

$ python student-listing.py

To update to the latest version:

$ wget -O student-listing.py https://raw.githubusercontent.com/saulbaizman-massart/repl-directory-index/master/student-listing.py
'''

import os

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
repl_map['omatheson99'] = ['Homework','Final-Project','Client-Website',]
repl_map['tanyaandreeva'] = ['Homework','Final-Project','Client-Website',]

page_title = 'student directory &mdash; fa20'

header='''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>%s</title>
    <style type="text/css">
    * { font-family: Helvetica, Arial, sans-serif }
    body { margin: 50px }
    ul ul { margin-bottom: 20px }
    li { line-height: 1.55em }
    a { text-decoration: none; color: red; font-weight: bold }
    a:hover, a:focus { background-color: rgba(250,0,0,.1) }
    body > div.grid_parent > div.student { list-style-type: none; list-style-position: inside ; padding-left: 0; font-size: 2rem; font-weight: bold; background-color: #eee; border-radius: 10px ; padding: 20px 20px 0 35px ; }
    body > div.grid_parent > div.student > section.links > ul { margin-top:0; padding-left: 0 }
    body > div.grid_parent > div.student > section.links > ul > li { font-size: 1rem; font-weight: normal }
    body > div.grid_parent > div.student > section.links > ul > li::marker { content: "— " }
    body > div.grid_parent > div.student > section.links > ul > li > span.separator { color: rgb(180,180,180) }
    body > div.grid_parent { display: grid; grid-template-columns: repeat(4,1fr); grid-template-rows: repeat(3,1fr); grid-auto-flow: column ; grid-gap: 30px }
    img.avatar { width: 128px; height: 128px; background-color: #888 ; border-radius: 50%%; box-shadow: 0 0 6px 3px #ccc }
    p.avatar_container { text-align: center; margin: 10px 0 }
    p.repl_user_link_container { text-align: center; margin: 10px 0 }
    </style>
  </head>
  <body>
    <h1>%s</h1>
''' % ( page_title, page_title )

footer='''
  </body>
</html>
'''

image_subfolder = 'img'

content = []

content.append('<div class="grid_parent">')

# loop through students
for student in sorted (name_map.keys()):
    real_name = student.lower()
    repl_username = name_map[student]
    
    image = '%s/%s.png' % ( image_subfolder, real_name )
    if not os.path.exists(image):
        image = '%s/blank.png' % image_subfolder
    content.append ( '<div class="student"><p class="avatar_container"><img class="avatar" src="%s" title="%s"></p>' % ( image, real_name ) )
    content.append ( '<section class="links">' )
    content.append ( '<p class="repl_user_link_container">%s</p>' % format_link ( 'repl.it/@%s' % repl_username, real_name ) )
    content.append('<ul>')

    # loop through each student's list of repls
    for repl in repl_map[repl_username]:
        repl_clean = repl.lower().replace('-',' ')
        content.append ( '<li>%s: %s <span class="separator">&bull;</span> %s</li>' % ( repl_clean, format_link('repl.it/@%s/%s/' % ( repl_username, repl ) , 'repl'), format_link('%s.%s.repl.co' % ( repl, repl_username ), 'website') ) )

    content.append('</ul>')
    content.append( '</section>' )
    content.append('</div>')

content.append('</div>')

# write to the file
index = open("index.html", "w")
index.write(header)
index.write("\n".join(content))
index.write(footer)
index.close()
