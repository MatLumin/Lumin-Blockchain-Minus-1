

from sqlite3 import Cursor, Connection

import make_connection_to_db

from Wallet import Wallet


def create(con:Connection, wallet:Wallet)->None:
    cur:Cursor = con.cursor()
    cur.execute(f'''
    INSERT INTO Wallet 
    (address, public_key_n, public_key_e)
    VALUES
    ({wallet.address}, "{wallet.public_key_n}", "{wallet.public_key_e}")
    ''')
    con.commit()
    return None




if __name__ == '__main__':
    create(
        make_connection_to_db.make(),
        Wallet("ABCD", 0)
    )