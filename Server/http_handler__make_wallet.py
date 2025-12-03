from typing import *
from sqlite3 import Connection

from rsa import PrivateKey

import get_wallet_count_from_db
from GLOBAL_CONST import MAX_WALLET_COUNT
import generate_Wallet
from Wallet import Wallet


def function(con:Connection)->Dict[str,Any]:
    wallet: Wallet
    private_key:PrivateKey
    wallet, private_key = generate_Wallet.generate(con)

    if wallet is None:
        return {
            "is_ok":False,
            "error_code":"WALLET_COUNT_REACHED_MAX",
            "caption":"wallet count has reached its maximum no wallet be issued anymore"
        }


    return {
        "is_ok":True,
        "data":{
            "private_key":{
                "n":private_key.n,
                "e":private_key.e,
                "d":private_key.d,
                "p":private_key.p,
                "q":private_key.q,
            },
            "address":wallet.address,
        }

    }
