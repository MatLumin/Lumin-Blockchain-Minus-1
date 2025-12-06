
from sqlite3 import Connection

from Transaction import Transaction
from GLOBAL_CONST import MAX_WALLET_COUNT
import does_wallet_exist_in_db
import is_transaction_valid_by_address_without_db


def check(con:Connection, t:Transaction)->str:
    #check if wallet even exists
    if does_wallet_exist_in_db.check(con, t.sender):
        return "SENDER_WALLET_DOES_NOT_EXIST"
    return is_transaction_valid_by_address_without_db.check(
        t=t
    )


