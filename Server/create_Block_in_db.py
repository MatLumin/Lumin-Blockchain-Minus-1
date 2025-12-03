

import sqlite3
from sqlite3 import Connection, Cursor

import GLOBAL_CONST
from Block import Block


def create(con:Connection, block:Block):
    #this function wont check if db file exists
    cur: Cursor = con.cursor()
    cur.execute(f'''
    
    INSERT INTO Block (
    amount,
    sender,
    receiver,
    sender_signature,
    previous_hash,
    "index",
    unix,
    nonce
    )
    VALUES (
    {block.amount},
    {block.sender},
    {block.receiver},
    "{block.sender_signature}",
    "{block.previous_hash}",
    {block.index},
    {block.unix},
    "{block.nonce}",
    );
    ''')
    con.commit()
    cur.close()


if __name__ == '__main__':
    b:Block = Block(
        amount=1,
        sender=0,
        receiver=1,
        sender_signature="SIGN",
        previous_hash="0",
        index=0,
        unix=0
    )
    con:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    create(con, b)
    con.close()