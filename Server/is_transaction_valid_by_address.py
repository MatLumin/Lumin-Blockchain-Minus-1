
from sqlite3 import Connection

from Transaction import Transaction
from GLOBAL_CONST import MAX_WALLET_COUNT
import does_wallet_exist_in_db


def check(con:Connection, t:Transaction)->bool:
    #will only check values not the authority or existence of addresses!

    #addresses must be interger, in range of 0 till 255 (bot inclusive)

    #sender part
    a:bool = 0 <= t.sender < MAX_WALLET_COUNT
    b:bool = isinstance(t.sender, int)
    d:bool = a & b


    #receiver part
    e:bool = 0 <= t.receiver < MAX_WALLET_COUNT
    f:bool = isinstance(t.receiver, int)
    h:bool = f & e


