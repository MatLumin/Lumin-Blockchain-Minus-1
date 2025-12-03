from typing import *
from sqlite3 import Connection

import read_all_Block_from_db
from Block import Block
from Wallet import Wallet
import make_connection_to_db
import read_all_Wallet_from_db


# note sending amout to a non existent, considers the sent amount burnt untill the wallet starts existing

def get(con:Connection)->Dict[int,int]:
    #where key is the address of wallet and amount is the balance
    output:Dict[int,int] = {}

    wallet:Wallet
    for wallet in read_all_Wallet_from_db.read(con):
        output[wallet.address]= 0


    block: Block
    for block in read_all_Block_from_db.read(con):
        if block.sender not in output:
            output[block.sender] = 0
        if block.receiver not in output:
            output[block.receiver] = 0


        output[block.sender] -= block.amount
        output[block.receiver] += block.amount
    return output


if __name__ == "__main__":
    con:Connection = make_connection_to_db.make()
    print(get(con))