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
repl_map['kadbril'] = ['Homework','Final-Project','Client-Website',]
repl_map['KerryBlanchard'] = ['Homework','Final-Project','Client-Website',]
repl_map['Motsuki1120'] = ['homework','final-project','client-website',]
repl_map['MeghanYip'] = ['Homework','FinalProject','client-website',]
repl_map['omatheson99'] = ['Homework','Final-Project','Client-Website',]
repl_map['tanyaandreeva'] = ['Homework','Final-Project','Client-Website2020.html',]

avatar_url_map = {}
avatar_url_map['cjray22'] = 'https://cdn.discordapp.com/avatars/754893931665424424/9dbc8742a3051b3e84f1474e35bd851e.png?size=256'
avatar_url_map['ceallard'] = 'https://cdn.discordapp.com/avatars/754856841950789682/09735bdb5d07f419fe97503e50c122dd.png?size=256'
avatar_url_map['DanielGrieco'] = 'https://cdn.discordapp.com/avatars/754821840848814201/f921a001a96cfb86117869415f039378.png?size=256'
avatar_url_map['EmSpaulding0707'] = 'https://cdn.discordapp.com/avatars/754881803780620348/737e32fc58a6ddb5402460d8c8ff9d46.png?size=256'
avatar_url_map['EmilyHCC'] = 'https://cdn.discordapp.com/avatars/751484235512283236/a6a54851bcc2be444f3b7e3569f0405e.png?size=256'
avatar_url_map['jponeillsantiag'] = 'https://cdn.discordapp.com/avatars/754914909623681136/cd433ce88ea1cc33a421871172de0339.png?size=256'
avatar_url_map['kadbril'] = 'https://cdn.discordapp.com/avatars/754863313824907294/2dfeb0d18cc8a052782cc7bf72dfa38f.png?size=256'
avatar_url_map['KerryBlanchard'] = 'https://cdn.discordapp.com/avatars/755047905567440908/295673f9238facf71a16e3348ed880cd.png?size=256'
avatar_url_map['Motsuki1120'] = 'https://cdn.discordapp.com/avatars/753627598336294951/e569cc06bc09c78a836824b4f9b366ed.png?size=256'
avatar_url_map['MeghanYip'] = 'https://cdn.discordapp.com/avatars/721434474239229953/39e7d6a919d3f7f3bc243d7b475c4ad7.png?size=256'
avatar_url_map['omatheson99'] = 'https://cdn.discordapp.com/avatars/754932634290749590/a8092606f1bd8f0a63d11eeefd528005.png?size=256'
avatar_url_map['tanyaandreeva'] = 'https://cdn.discordapp.com/avatars/754876730870857798/c8d13066a8ff42b256dcb3cdb922bbde.png?size=256'

page_title = 'fa20 student directory'

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
    body > div.grid_parent > div.student { list-style-type: none; list-style-position: inside ; padding-left: 0; font-size: 2rem; font-weight: bold; background-color: #eee; border-radius: 10px ; padding: 20px 30px 0 30px ; }
    body > div.grid_parent > div.student > section.links > ul { margin-top:0; padding-left: 0 }
    body > div.grid_parent > div.student > section.links > ul > li { font-size: 1rem; font-weight: normal }
    body > div.grid_parent > div.student > section.links > ul > li::marker { content: "— " }
    body > div.grid_parent > div.student > section.links > ul > li > span.separator { color: rgb(180,180,180) }
    body > div.grid_parent { display: grid; grid-template-columns: repeat(4,1fr); grid-template-rows: repeat(3,1fr); grid-auto-flow: column ; grid-gap: 30px }
    img.avatar { width: 128px; height: 128px; background-color: #888 ; border-radius: 50%%; box-shadow: 0 0 6px 3px #ccc }
    p.avatar_container { text-align: center; margin: 10px 0 }
    p.avatar_container a:hover, p.avatar_container a:focus { background-color: rgba(250,0,0,0) }
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

content = []

content.append('<div class="grid_parent">')

# loop through students
for student in sorted (name_map.keys()):
    # the student's first name
    real_name = student.lower()
    # the student's repl username
    repl_username = name_map[student]
    # image url that lives on discord
    image = avatar_url_map[repl_username]
    content.append ( '<div class="student"><p class="avatar_container">%s</p>' % format_link ( 'repl.it/@%s' % repl_username, '<img class="avatar" src="%s" title="%s">' % ( image, real_name ) ) )
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
