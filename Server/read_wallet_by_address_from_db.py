from sqlite3 import Connection
from typing import *

from Wallet import Wallet
import read_all_Wallet_from_db


def read(con:Connection, address:int)->Union[None,Wallet]:
    all_wallet:List[Wallet] = read_all_Wallet_from_db.read(con)
    output:Union[None,Wallet] = None
    for i in all_wallet:
        if i.address == address:
            output = i
            break
    return output