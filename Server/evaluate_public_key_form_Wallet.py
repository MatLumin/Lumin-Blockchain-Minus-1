


import rsa
from rsa import PublicKey

from Wallet import Wallet


def evaluate(wallet:Wallet)->PublicKey:
    return PublicKey(n=wallet.n, e=wallet.e)