#!/usr/bin/env python2.7


import cgi
import cgitb
import MySQLdb
from string import Template

import pre
from mysqlopts import give_mysql_opts
from run_props import get_av_speed

from parsegpx import parse_gpx

mysql_opts = give_mysql_opts()
mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db'])
cur = mysql.cursor()

arguments = cgi.FieldStorage()
if "action" in arguments:
    action = arguments.getvalue("action")
else:
    action = "runs"

print '"' + action + '"'

if action == 'runs':
    headline = "L&auml;ufe"
    html =  """                                                                                                                                           
<div id='mitte_unten'>                                                                                                                                    
    <p style="margin-left:15px;">                                                                                                                         
                                                                                                                                                          
    </p>                                                                                                                                                  
<h1><span class='hToggle' onclick='ToggleBox("bla")'>$headline <span class='hInfo'></span></span></h1> <div class='suchbox' id='search_form' style='background-color=#00ccff;display:block;'>                                                                                                                      
"""

    s = Template(html).safe_substitute(headline = headline)

    print s

    print "<h2>Neuen Lauf eintragen</h2>"

    runs_order = list()

    cur.execute ("SELECT id FROM run ORDER BY date;")
    res = cur.fetchall()
    for row in res:
        runs_order.append(row[0])

    cur.execute("SELECT run_id, run.date, human.name, dog.name, track.name, track.distance, track.alt_diff, run.run_type, run_dogs.position, run.class, run.time, run.gpx_file FROM run_dogs INNER JOIN run ON run_id = run.id INNER JOIN dog ON dog_id = dog.id INNER JOIN track ON run.track_id = track.id INNER JOIN human ON run.human_id = human.id ORDER BY date DESC;")
    res = cur.fetchall()

    runs_ord = list()
    runs = dict()

    for row in res:
        if not row[0] in runs:
            runs_ord.append(row[0])
            runs[row[0]] = dict()
            runs[row[0]]["track"] = dict()
            runs[row[0]]["dog"] = dict()
            
        runs[row[0]]["date"] = row[1]
        runs[row[0]]["human"] = row[2]
        runs[row[0]]["type"] = row[7]
        runs[row[0]]["track"]["name"] = row[4]
        runs[row[0]]["track"]["distance"] = row[5]
        runs[row[0]]["track"]["alt_diff"] = row[6]
        runs[row[0]]["dog"][row[8]] = row[3]
        runs[row[0]]["class"] = row[9]
        runs[row[0]]["time"] = row[10]
        runs[row[0]]["gpx"] = row[11]
        
        
    print "<h2>&Uuml;bersicht L&auml;ufe</h2>"
    # CREATE RUN-DETAIL BOXES HIDED BY DEFAULT
    for r in runs_ord:
        print "<div id='div_%s' style='display:none;'> "%(r)
        svg = str()
        distance = 0.0
        print "<span class='hToggle' onclick='ToggleBox(\"div_%s\")'><h2>Details <small>%s</small></h2></span>"%(r,runs[r]["date"])
        print "<table>"
        print "<tr><td>Musher</td><td>%s</td></tr>"%(runs[r]["human"])
        print "<tr><td>Strecke</td><td>%s</td></tr>"%(runs[r]["track"]["name"])
        print "<tr><td>Streckenl&auml;nge [km]</td><td>%s</td></tr>"%(runs[r]["track"]["distance"])
        print "<tr><td>H&ouml;henmeter [m]</td><td>%s</td></tr>"%(runs[r]["track"]["alt_diff"])
        print "<tr><td>Zeit [hh:mm:ss]</td><td>%s</td></tr>"%(runs[r]["time"])

        print "<tr><td>Durchschnittsgeschwindigkeit [km/h]</td><td>%s</td></tr>"%(get_av_speed(runs[r]["track"]["distance"],runs[r]["time"])  )
        print "<tr><td>Klasse</td><td>%s</td></tr>"%(runs[r]["class"])
        print "<tr><td>Art des Laufs</td><td>%s</td></tr>"%(runs[r]["type"])

        print "</table>"
        if not runs[r]["gpx"] == None:
            distance,svg,map3d, map2d = parse_gpx(runs[r]["gpx"])
            print "H&oumlhendiagramm<br>"
            print svg
            print "<br>"
            print "3d-Karte<br>"
            print map3d
            print "<br>"
            print "2d-Karte<br>"
            print map2d
        print "</div>"

    # PRINT TABLE WITH RUNS
    print "<table><tr><th>Datum</th><th>Musher</th><th>Klasse</th><th>Hund/e</th><th>Strecke</th><th>Art des Laufs</th></tr>"

    for r in runs_ord:
        print "<tr><td> <span class='hToggle' onclick='ToggleBox(\"div_%s\")'>%s</td><td>%s</td><td>%s</td><td><table>"%(r,runs[r]["date"],runs[r]["human"],runs[r]["class"])
        for d in runs[r]["dog"]:
            print "<tr><td style='width:60px;' align='left'>%s</td><td style='width:100px;' align='left'>%s</td></tr>"%(runs[r]["dog"][d],d)
        print "</table></td><td>%s</td><td>%s</span></td></tr>"%(runs[r]["track"]["name"], runs[r]["type"])
            


    print "</table>"

        
if action == 'dogs':
    headline = 'Hunde'

    cur.execute("SELECT dog.name, dog.birth_date, dog.father, dog.mother, human.name, dog.grower, dog.growers_name, dog.id FROM dog INNER JOIN human ON owner_id = human.id;")
    dogs = cur.fetchall()


#    print dogs
    # CREATE BOX FOR CONTENT
    html =  """                                                                                                                                           
<div id='mitte_unten'>                                                                                                                                    
    <p style="margin-left:15px;">                                                                                                                         
                                                                                                                                                          
    </p>                                                                                                                                                  
<h1><span class='hToggle' onclick='ToggleBox("bla")'>$headline <span class='hInfo'></span></span></h1> <div class='suchbox' id='search_form' style='background-color=#00ccff;display:block;'>                                                                                                                      
"""

    s = Template(html).safe_substitute(headline = headline)
    print s

    for dog in dogs:
        sql = "SELECT run.run_type, run.time, run.class, track.distance, track.alt_diff FROM run_dogs INNER JOIN run ON run_id = run.id INNER JOIN track ON run.track_id = track.id WHERE dog_id = %s;"%dog[7] 
        cur.execute(sql)
        dog_det = cur.fetchall()
        av_speed = dict()
        for det in dog_det:
            if not det[0] in av_speed:
                av_speed[det[0]] = list()
            av_speed[det[0]].append(str(det[3]) + ";" + str(get_av_speed(det[3], det[1])))

        
        print "<div id='div_%s' style='display:none;'> "%(dog[7])
        print "<span class='hToggle' onclick='ToggleBox(\"div_%s\")'><h2>Statistik <small>%s</small></h2></span>"%(dog[7], dog[0])
        print av_speed
        print "</div>"

    print "<table><tr><th>Name</th><th>Datum der Geburt</th><th>Besitzer</th><th>Z&uuml;chter</th><th>Vater</th><th>Mutter</th><th>Zuchtname</th></tr>"
    for dog in dogs:
        html = "<tr><td><span onclick='ToggleBox(\"$div\")'>$Name</span></td><td>$DoB</td><td>$Own</td><td>$Grow</td><td>$Fat</td><td>$Mot</td><td>$Grow_N</td></tr>"
        s = Template(html).safe_substitute(div = "div_%s"%dog[7], Name = dog[0], DoB = str(dog[1]).split(" ")[0], Own = dog[4], Grow = dog[5], Fat = dog[2], Mot = dog [3], Grow_N = dog[6])
        print s

    
        
    print "</table>"
    print "</div><div class='suchbox' id='search_form' style='background-color=#00ccff;display:block;'>"
    print "<h2>Neuen Hund eintragen</h2>"

    print "<form action='create_new_dog.py' method='POST'><table>"
    
    print "<tr><td>Name:</td><td><input type='text' name='name' size='30'/></td></tr>"
    print "<tr><td>Besitzer:</td><td><input type='text' name='owner' size='30'/></td></tr>"
    print "<tr><td>Geburtsdatum (YYYY-MM-DD):</td><td><input type='text' name='birthdate' size='30' value='2001-01-01'/></td></tr>"
    print "<tr><td>Z&uuml;chter:</td><td><input type='text' name='grower' size='30'/></td></tr>"
    print "<tr><td>Vater:</td><td><input type='text' name='father' size='30'/></td></tr>"
    print "<tr><td>Mutter:</td><td><input type='text' name='mother' size='30'/></td></tr>"
    print "<tr><td>Zuchtname:</td><td><input type='text' name='growers_name' size='30'/></td></tr>"
    
    print "<tr><td></td><td><button type='submit'>Eintragen</submit></td></tr>"

    print "</div></div>"

mysql.close()
import post
