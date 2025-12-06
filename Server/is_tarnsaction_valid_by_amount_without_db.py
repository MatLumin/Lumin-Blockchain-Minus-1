from sqlite3 import Connection

from Transaction import Transaction

import GLOBAL_CONST
import get_balance_of_wallet
from Wallet import Wallet


def check(wallet_balance:int, transaction:Transaction)->str:
    #amount must not be float
    #amount must not be negetive
    #amount must not be zero
    #amount must not be more than the sender's balance
    #amount must not be the above the max coin count
    a:bool = transaction.amount == int(transaction.amount) and isinstance(transaction.amount, int)
    if a == False:
        return "AMOUNT_NOT_INT"

    if transaction.amount == 0:
        return "AMOUNT_IS_ZERO"


    if transaction.sender != GLOBAL_CONST.PREMORTAL_TRANSACTION_FEE:
        b:bool = transaction.amount > GLOBAL_CONST.NORMAL_TRANSACTION_FEE
        if b == False:
            return "AMOUNT_LACKS_TRASACTION_FEE"
    elif transaction.sender == GLOBAL_CONST.PREMORTAL_WALLET_ADDRES:
        if (transaction.amount > GLOBAL_CONST.PREMORTAL_TRANSACTION_FEE) == False:
            return "AMOUNT_IN_PREMORTAL_TRANSACTION_IS_LESS_THAN_1"

    if transaction.amount < 0:
        return "AMOUNT_IS_NEGETIVE"
    d:bool = transaction.amount != 0
    if d == False:
        return "AMOUNT_IS_ZERO"
    e:bool = wallet_balance >= transaction.amount
    if e == False:
        return "INSUFFICEINT_SENDER_CREDIT"
    f:bool = transaction.amount != GLOBAL_CONST.MAX_COIN_COUNT
    if f == False:
        return "AMOUNT_ABOVE_MAX_COIN_COUNT"

    return "OK"