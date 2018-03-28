#!/usr/bin/env python2.7

import cgi
import MySQLdb
import datetime
from mysqlopts import give_mysql_opts, give_item_id

mysql_opts = give_mysql_opts()
mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db'])
cur = mysql.cursor()

arguments = cgi.FieldStorage()

write_to_db = 1

print "Content-type: text/html\n\n"

name = arguments.getvalue("name")
owner = arguments.getvalue("owner")
birthdate = arguments.getvalue("birthdate")
grower = arguments.getvalue("grower")
father = arguments.getvalue("father")
mother = arguments.getvalue("mother")
growers_name = arguments.getvalue("growers_name")


print name
print "\n________\n" 

print owner
print "________" 

print birthdate
print "________" 

print grower
print "________" 

print father
print "________" 

print mother
print "________" 

print growers_name
print "________" 

if name == None or name == "None":
    import sys
    sys.exit()
    
if owner == None or owner == "None":
    import sys
    sys.exit

owner_id = give_item_id(owner,"name","human", 1)
print owner_id

birthdate = str(birthdate).replace("-", "") + "000000"

sql = "INSERT INTO dog (name, birth_date, father, mother, owner_id, grower, growers_name) VALUES ('%s',%s, '%s', '%s', %s, '%s', '%s');" % (name, birthdate, father, mother, owner_id, grower, growers_name)

if write_to_db ==1:
    cur.execute(sql)
    mysql.commit()
else:
    print sql

mysql.close()
