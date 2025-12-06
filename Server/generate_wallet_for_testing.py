from typing import *

import rsa
from rsa import PrivateKey, PublicKey

import GLOBAL_CONST
from Wallet import Wallet

#wont store anything in db

def generatre(address:int)->Tuple[Wallet, PrivateKey]:

    pub:rsa.PublicKey
    priv:rsa.PrivateKey
    (pub, priv) = rsa.newkeys(GLOBAL_CONST.WALLET_KEY_LENGTH)

    w = Wallet(
        public_key_n=pub.n,
        public_key_e=int(pub.e),
        address=address
    )

    return [w, priv]