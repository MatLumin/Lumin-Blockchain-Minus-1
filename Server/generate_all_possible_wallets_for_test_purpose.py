from typing import *

import rsa

import GLOBAL_CONST
from Wallet import Wallet

#wont sore anything in db

def generatre()->Tuple[List[Wallet], List[str]]:
    i:int
    output_wallets:List[Wallet] = []
    output_priv_keys:List[PrivateKey] = []
    for i in range(0, GLOBAL_CONST.MAX_WALLET_COUNT):
        print(i)
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