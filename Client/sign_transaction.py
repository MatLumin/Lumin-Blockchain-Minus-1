import base64

import rsa
from rsa import PrivateKey

import eval_private_key_from_config
from Transaction import Transaction
import scramble_transaction


def sign(t:Transaction)->str: #will reteun a base64 encoded signature
    priv:PrivateKey = eval_private_key_from_config.eval()
    signature:bytes = rsa.sign(scramble_transaction.scramble(t), priv, 'SHA-256')
    return base64.b64encode(signature).decode(encoding='ascii')