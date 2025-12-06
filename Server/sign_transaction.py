import base64

import rsa
from rsa import PrivateKey, PublicKey

import GLOBAL_CONST
from Wallet import Wallet
from Transaction import Transaction
import scramble_transaction
import turn_bytes_to_base64_string


def sign(t:Transaction, private_key:PrivateKey, wallet_of_sender:Wallet)->str: #will reteun a base64 encoded signature
    """
    exit codes:
        OK
        TRANSACTION_SENDER_DOES_NOT_MATCH_WALLET_ADDRS
    """
    if t.sender != wallet_of_sender.address:
        return "TRANSACTION_SENDER_DOES_NOT_MATCH_WALLET_ADDRS"


    signature:bytes = rsa.sign(scramble_transaction.scramble(t), private_key, GLOBAL_CONST.SIGNING_HASH_ALGHO_NAME)
    t.sender_signature = turn_bytes_to_base64_string.turn(signature)
    return "OK"

