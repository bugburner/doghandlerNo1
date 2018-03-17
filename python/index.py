#!/usr/bin/env python2.7


import cgi
import cgitb;
import MySQLdb

from string import Template

def give_mysql_opts(): 
    mysql_opts = {
        'host': "localhost",
        'user': "doghandler",
        'pass': "doghandler_blarg0815",
        'db':   "doghandlerNo1"
        }
    return mysql_opts

import pre

import mysqlopts

mysql_opts = give_mysql_opts()
mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db'])
cur = mysql.cursor()

arguments = cgi.FieldStorage()
if "action" in arguments:
    action = arguments.getvalue("action")
else:
    action = "Overview"

print '"' + action + '"'
    
if action == 'dogs':
    headline = 'Hunde'

    cur.execute("SELECT dog.name, dog.birth_date, dog.father, dog.mother, human.first_name, human.last_name, dog.grower, dog.growers_name FROM dog INNER JOIN human ON owner_id = human.id;")
    dogs = cur.fetchall()

    print dogs
    # CREATE BOX FOR CONTEN                                                                                                                                   
    html =  """                                                                                                                                           
<div id='mitte_unten'>                                                                                                                                    
    <p style="margin-left:15px;">                                                                                                                         
                                                                                                                                                          
    </p>                                                                                                                                                  
<h1><span class='hToggle' onclick='ToggleBox("bla")'>$headline <span class='hInfo'></span></span></h1> <div class='suchbox' id='search_form' style='backg\
round-color=#00ccff;display:block;'>                                                                                                                      
"""

    s = Template(html).safe_substitute(headline = headline)
    print s

#    print html
    print "<table><tr><th>Name</th><th>Datum der Geburt</th><th>Besitzer</th><th>Z&uuml;chter</th><th>Vater</th><th>Mutter</th><th>Zuchtname</th></tr>"
    for dog in dogs:
        html = "<tr><td>$Name</td><td>$DoB</td><td>$Own</td><td>$Grow</td><td>$Fat</td><td>$Mot</td><td>$Grow_N</td></tr>"
        s = Template(html).safe_substitute(Name = dog[0], DoB = dog[1], Own = str(dog[4] + ' ' + dog[5]), Grow = dog[6], Fat = dog[2], Mot = dog [3], Grow_N = dog[7])
        print s
        #print dog
        
    print "</table>"
    print "</div></div>"

import post
