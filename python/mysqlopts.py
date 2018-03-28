import MySQLdb

def give_mysql_opts(): 
    mysql_opts = {
        'host': "localhost",
        'user': "doghandler",
        'pass': "doghandler_blarg0815",
        'db':   "doghandlerNo1"
        }
    return mysql_opts

def give_item_id(name, option, item, write):
    mysql_opts = give_mysql_opts()
    mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db'])
    cur = mysql.cursor()
    
    sql = "SELECT id FROM %s WHERE %s = '%s';"%(item, option, name)
    
    cur.execute(sql)
    res = cur.fetchall()
    
    id = 0
    if len(res) > 1:
        print "ERROR: More than one Items found with this Name"
    if len(res) == 0:
        print "ERROR No Item found with this name!"
    else:
        for r in res:
            id = r[0]

    return id
    
