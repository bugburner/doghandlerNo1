#!/usr/bin/python2.7

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



import post
