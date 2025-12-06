import base64

import rsa
from rsa import PrivateKey, PublicKey

from Transaction import Transaction
from Wallet import Wallet
import turn_base64_string_to_bytes
import scramble_transaction
import evaluate_public_key_form_Wallet
import generate_wallet_for_testing
import sign_transaction
import GLOBAL_CONST


def verify(t:Transaction, sender_wallet:Wallet)->str:
    #dont call this function for premortal tranactions 
    """
    EXIT CODES:
        "PASSED"
        "FAILED"
        "SENDER_SIGNATURE_DOES_NOT_MATCH_SENDER_WALLET_ADDRESS"
    """
    sgnature_as_bytes:bytes = turn_base64_string_to_bytes.turn(t.sender_signature)
    if t.sender != sender_wallet.address:
        return "SENDER_SIGNATURE_DOES_NOT_MATCH_SENDER_WALLET_ADDRESS"
    pub_key:PublicKey = evaluate_public_key_form_Wallet.evaluate(wallet=sender_wallet)
    result:bool = GLOBAL_CONST.SIGNING_HASH_ALGHO_NAME == rsa.verify(
        message=scramble_transaction.scramble(t),
        signature=sgnature_as_bytes,
        pub_key=pub_key
    )

    if result == True:
        return "PASSED"
    if result == False:
        return "FAILED"


if __name__ == "__main__":
    w:Wallet
    priv:PrivateKey
    w, priv = generate_wallet_for_testing.generatre(0)

    t:Transaction = Transaction(
        sender=0,
        receiver=1,
        sender_signature=None,
        amount=2
    )

    sign_transaction.sign(t)

    verify()