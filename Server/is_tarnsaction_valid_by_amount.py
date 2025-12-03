from sqlite3 import Connection

from Transaction import Transaction

import GLOBAL_CONST
import get_balance_of_wallet


def check(con:Connection, transaction:Transaction)->str:
    #amount must not be float
    #amount must not be negetive
    #amount must not be zero
    #amount must not be more than the sender's balance
    #amount must not be the above the max coin count
    a:bool = transaction.amount == int(transaction.amount) and isinstance(transaction.amount, int)
    if a == False:
        return "AMOUNT_NOT_INT"
    c:bool = transaction.amount > 0
    if c == False:
        return "AMOUNT_IS_NEGETIVE"
    d:bool = transaction.amount != 0
    if d == False:
        return "AMOUNT_IS_ZERO"
    e:bool = get_balance_of_wallet.get(con, address=transaction.sender) >= transaction.amount
    if e == False:
        return "INSUFFICEINT_SENDER_CREDIT"
    f:bool = transaction.amount != GLOBAL_CONST.MAX_COIN_COUNT
    if f == False:
        return "AMOUNT_ABOVE_MAX_COIN_COUNT"
    return "OK"