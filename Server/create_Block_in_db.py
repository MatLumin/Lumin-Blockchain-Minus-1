

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
    nonce,
    pow_algho_name,
    pow_algho_difficulty
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
    "{block.pow_algho_name}",
    {block.pow_algho_difficulty}
    );
    ''')
    con.commit()
    cur.close()


if __name__ == '__main__':
    con:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    i:int
    for i in range(0,100):
        b:Block = Block(
            amount=1,
            sender=0,
            receiver=1,
            sender_signature="SIGN",
            previous_hash="0",
            index=i,
            unix=0,
            nonce="0",
            pow_algho_name="LEADING_ZERO",
            pow_algho_difficulty=4,

        )

        create(con, b)
    con.close()