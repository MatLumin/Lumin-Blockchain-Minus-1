

import sqlite3
from sqlite3 import Connection,Cursor


import GLOBAL_CONST


def define()->None:
    con:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    cur:Cursor = con.cursor()
    cur.execute('''
    CREATE TABLE "Wallet" (
        "address"	INTEGER,
        "public_key_n"	TEXT,
        "public_key_e"	TEXT,
        PRIMARY KEY("address")
    );
    ''')
    con.commit()
    cur.close()
    con.close()
    return None



if __name__ == '__main__':
    define()

