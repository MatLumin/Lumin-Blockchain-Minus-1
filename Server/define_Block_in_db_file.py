

import sqlite3
from sqlite3 import Connection, Cursor

import GLOBAL_CONST




def define()->None:
    #note this function will not check if db file exits!
    #note this function may not be called when db file alredy exists
    con:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    cur:Cursor = con.cursor()
    cur.execute('''
CREATE TABLE "Block" (
	"amount"	INTEGER NOT NULL,
	"sender"	INTEGER NOT NULL,
	"receiver"	INTEGER NOT NULL,
	"sender_signature"	TEXT NOT NULL,
	"index"	INTEGER NOT NULL UNIQUE,
	"unix"	INTEGER NOT NULL,
	"previous_hash"	TEXT NOT NULL,
	"nonce" TEXT NOT NULL,
	PRIMARY KEY("index")
);
    ''')
    con.commit()
    cur.close()
    con.close()
    return None


if __name__ == "__main__":
    define()