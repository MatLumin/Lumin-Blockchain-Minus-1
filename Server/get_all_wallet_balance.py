from typing import *
from sqlite3 import Connection

import read_all_Block_from_db
from Block import Block
from Wallet import Wallet
import make_connection_to_db
import read_all_Wallet_from_db
import get_all_wallet_balance_without_db


#note this function reads from db a non-db variant do exist


def get(con:Connection)->Dict[int,int]:
    #where key is the address of wallet and amount is the balance
    output:Dict[int,int] = {}

    wallet:Wallet
    for wallet in read_all_Wallet_from_db.read(con):
        output[wallet.address]= 0

    get_all_wallet_balance_without_db.get(blocks=read_all_Block_from_db.read(con))

    return output


if __name__ == "__main__":
    con:Connection = make_connection_to_db.make()
    print(get(con))