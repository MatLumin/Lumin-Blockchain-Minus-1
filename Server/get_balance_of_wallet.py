from typing import *
from sqlite3 import Connection

import get_all_wallet_balance
import make_connection_to_db

def get(con:Connection, address:int)->int:
    #will retunr -1 if wallet not found
    all_wallet_balance:Dict[int,int] = get_all_wallet_balance.get(con)
    if (address in all_wallet_balance) == False:
        return -1

    return all_wallet_balance[address]



if __name__ == "__main__":
    con = make_connection_to_db.make()
    print(get(con, 0))