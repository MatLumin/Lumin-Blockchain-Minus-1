from typing import *
from sqlite3 import Connection

import rsa
from rsa import PrivateKey

from Wallet import Wallet
import get_wallet_count_from_db
from GLOBAL_CONST import MAX_WALLET_COUNT
import create_Wallet_in_db


#will also store it in db

def generate(con:Connection)->Tuple[Union[None, Wallet], Union[None, PrivateKey]]:
    #will return a tuple where first is the wallet object and second is the private key object
    #will be a tuple of both None in wallet count has reached max
    wallet_count: int = get_wallet_count_from_db.get(con=con)
    if wallet_count == MAX_WALLET_COUNT:
        return None

    (pub, priv) = rsa.newkeys(1024)

    w = Wallet(
        public_key_n=pub.n,
        public_key_e=int(pub.e),
        address=int(wallet_count)
    )

    create_Wallet_in_db.create(
        con=con,
        wallet=w
    )

    return [w, priv]