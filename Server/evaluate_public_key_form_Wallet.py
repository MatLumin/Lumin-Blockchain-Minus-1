


import rsa
from rsa import PublicKey

from Wallet import Wallet


def evaluate(wallet:Wallet)->PublicKey:
    return PublicKey(n=wallet.public_key_n, e=wallet.public_key_e)


