
from sqlite3 import Connection

from Transaction import Transaction
from GLOBAL_CONST import MAX_WALLET_COUNT
import does_wallet_exist_in_db


def check(t:Transaction)->str:


    #will only check values not the authority or existence of addresses!

    #addresses must be interger, in range of 0 till 255 (bot inclusive)

    #sender part

    a:bool = 0 <= t.sender < MAX_WALLET_COUNT
    if a == False:
        return "SENDER_ADDRESS_NOT_IN_VALID_RANGE"
    b:bool = isinstance(t.sender, int)
    if b == False:
        return "SENDER_ADDRESS_IS_NOT_INT"

    #receiver part
    e:bool = 0 <= t.receiver < MAX_WALLET_COUNT
    if e == False:
        return "RECEIVER_ADDRESS_NOT_IN_VALID_RANGE"
    f:bool = isinstance(t.receiver, int)
    if f == False:
        return "RECEIVER_ADDRESS_IS_NOT_INT"

    if t.sender == t.receiver:
        return "SENDER_AND_RECEIVER_THE_SAME"

    return "OK"


