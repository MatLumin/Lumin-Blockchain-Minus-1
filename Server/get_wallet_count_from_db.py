
from sqlite3 import Connection, Cursor


import make_connection_to_db

def get(con:Connection):
    cur:Cursor = con.cursor()
    cur.execute('select count(*) from Wallet')
    output = cur.fetchone()[0]
    cur.close()
    return output






if __name__=='__main__':
    con:Connection = make_connection_to_db.make()
    print(get(con))