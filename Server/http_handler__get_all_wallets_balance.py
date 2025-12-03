from typing import *

from sqlite3 import Connection


from Wallet import Wallet
import read_all_Wallet_from_db
import get_all_wallet_balance


def function(con:Connection)->Dict[int,int]:
    output:str = """"""
    balance:Dict[int,int] = get_all_wallet_balance.get(con)
    return {
        "is_ok":True,
        "data":balance,
    }