from sqlite3 import Connection

from Transaction import Transaction

import GLOBAL_CONST
import get_balance_of_wallet
from Wallet import Wallet


def check(wallet_balance:int, transaction:Transaction)->str:
    #wallet_balance is the balance of sender

    """
    NOTE:
        as you know balance of prenortal wallet is always negetive or zero (meaning coins going only out of wallet)
        therefore when cheking the credit of premortal wallet for transaction
        we have to simple subtract the given wallet balnce by max_coin_count
        and the resultant will be the amount of coins left in it
    """

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


    if transaction.sender != GLOBAL_CONST.PREMORTAL_WALLET_ADDRES:
        b:bool = transaction.amount > GLOBAL_CONST.NORMAL_TRANSACTION_FEE
        if b == False:
            return "AMOUNT_LACKS_TRASACTION_FEE"
    elif transaction.sender == GLOBAL_CONST.PREMORTAL_WALLET_ADDRES:
        if (transaction.amount != GLOBAL_CONST.PREMORTAL_MINING_REWARD):
            return "AMOUNT_IN_PREMORTAL_TRANSACTION_MUST_EQUAL_THE_CONSTATNT_REWARD"

    if transaction.amount < 0:
        return "AMOUNT_IS_NEGETIVE"
    d:bool = transaction.amount != 0
    if d == False:
        return "AMOUNT_IS_ZERO"
    if transaction.sender != GLOBAL_CONST.PREMORTAL_WALLET_ADDRES:
        if wallet_balance < transaction.amount:
            return "INSUFFICEINT_SENDER_CREDIT"
    elif transaction.sender == GLOBAL_CONST.PREMORTAL_WALLET_ADDRES:
        coins_remaining_in_premortal_wallet:int = GLOBAL_CONST.MAX_COIN_COUNT - wallet_balance
        if coins_remaining_in_premortal_wallet < GLOBAL_CONST.PREMORTAL_MINING_REWARD:
            return "INSUFFICEINT_COINS_IN_PREMORTAL_WALLET_TO_EXTRACT_FROM"
    f:bool = transaction.amount != GLOBAL_CONST.MAX_COIN_COUNT
    if f == False:
        return "AMOUNT_ABOVE_MAX_COIN_COUNT"

    return "OK"