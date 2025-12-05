from typing import *
from sqlite3 import Connection

import rsa
from rsa import PrivateKey

from Wallet import Wallet
import get_wallet_count_from_db
import GLOBAL_CONST
from GLOBAL_CONST import MAX_WALLET_COUNT
import create_Wallet_in_db


#will also store it in db

def generate(con:Connection, dont_store_in_db:bool=True)->Tuple[Union[None, Wallet], Union[None, PrivateKey]]:
    #will return a tuple where first is the wallet object and second is the private key object
    #will be a tuple of both None in wallet count has reached max
    wallet_count: int = get_wallet_count_from_db.get(con=con)
    if wallet_count == MAX_WALLET_COUNT:
        return None

    (pub, priv) = rsa.newkeys(GLOBAL_CONST.WALLET_KEY_LENGTH)

    w = Wallet(
        public_key_n=pub.n,
        public_key_e=int(pub.e),
        address=int(wallet_count)
    )

    if dont_store_in_db == True:
        create_Wallet_in_db.create(
            con=con,
            wallet=w
        )

    return [w, priv]