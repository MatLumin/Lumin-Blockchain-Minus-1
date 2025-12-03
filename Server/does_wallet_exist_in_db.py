
from sqlite3 import Connection


import read_wallet_by_address_from_db
from Wallet import Wallet


def check(con:Connection, address:int)->bool:
    wallet:Wallet = read_wallet_by_address_from_db.read(con, address)
    if wallet is None:
        return False
    else:
        return True