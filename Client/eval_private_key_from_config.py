
from rsa import PrivateKey

import config



def eval()->PrivateKey:
    return PrivateKey(
        d=config.PRIVATE_KEY_D,
        e=config.PRIVATE_KEY_E,
        n=config.PRIVATE_KEY_N,
        p=config.PRIVATE_KEY_P,
        q=config.PRIVATE_KEY_Q,
    )