from typing import *

import sqlite3
from sqlite3 import Connection,Cursor

import GLOBAL_CONST
from Block import Block


def read(con:Connection)->List[Block]:
    output:List[Block] = []

    cur:Cursor = con.cursor()
    cur.execute("""
    SELECT 
        amount,
        sender,
        receiver,
        sender_signature,
        "index",
        unix,
        previous_hash,
        nonce
    FROM Block
    """)
    data:List[Tuple] = cur.fetchall()
    for row in data:
        output.append(
            Block(
                amount=row[0],
                sender=row[1],
                receiver=row[2],
                sender_signature=row[3],
                index=row[4],
                unix=row[5],
                previous_hash=row[6],
                nonce=row[7],
            )
        )

    cur.close()
    return output


if __name__ == '__main__':
    con:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    print(read(con))
    con.close()