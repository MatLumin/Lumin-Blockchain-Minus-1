import rsa
from rsa import PublicKey
PublicKey

import hash as hasher


def sign(content:bytes, private_key:bytes)->bytes:
    hashed:bytes = hasher.hash(content)
    signed:bytes = rsa.encrypt(hashed, pub_key=private_key)