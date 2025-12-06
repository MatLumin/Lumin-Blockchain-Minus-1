from typing import *

import rsa
from rsa import PrivateKey, PublicKey

import GLOBAL_CONST
from Wallet import Wallet

#wont store anything in db

def generatre()->Tuple[List[Wallet], List[PrivateKey]]:
    i:int
    output_wallets:List[Wallet] = []
    output_priv_keys:List[PrivateKey] = []
    for i in range(0, GLOBAL_CONST.MAX_WALLET_COUNT):
        pub:rsa.PublicKey
        priv:rsa.PrivateKey
        (pub, priv) = rsa.newkeys(GLOBAL_CONST.WALLET_KEY_LENGTH)

        w = Wallet(
            public_key_n=pub.n,
            public_key_e=int(pub.e),
            address=i
        )

        output_wallets.append(w)
        output_priv_keys.append(priv)



    return [output_wallets, output_priv_keys]


if __name__ == "__main__":
    print(generatre())