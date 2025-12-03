

from sqlite3 import Connection, Cursor
import sqlite3


import GLOBAL_CONST


"""
opens a sqlite cnnection
the opens a cursor
executes a command on it
then commits it
and close all the objects remaining
so you dont have to do it all the time
"""



#note this function is not thread safe!
#call it only when you are sure no other connection is made to sqlite3



def do_it(command:str)->None:
    con:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    cur:Cursor = con.cursor()
    cur.execute(command)
    con.commit()
    cur.close()
    con.close()
    return None


