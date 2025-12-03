from typing import *

from sqlite3 import Connection, Cursor

from Wallet import Wallet
import make_connection_to_db



def read(con:Connection)->List[Wallet]:

    output:List[Wallet] = []
    cur:Cursor = con.cursor()
    cur.execute('select address, public_key_n, public_key_e from Wallet')
    data:List[Tuple] = cur.fetchall()
    for (address, public_key_n, public_key_e) in data:
        output.append(Wallet(
            address=address,
            public_key_n=public_key_n,
            public_key_e=public_key_e
            )
        )
    return output


if __name__ == '__main__':
    con:Connection = make_connection_to_db.make()
    print(read(con))