import base64
from typing import *
from sqlite3 import Connection

from flask.wrappers import Request
import rsa
from rsa import PrivateKey, PublicKey

from Wallet import Wallet
from Transaction import Transaction
import does_wallet_exist_in_db
import read_wallet_by_address_from_db
import is_transaction_valid_by_address
import is_tarnsaction_valid_by_amount
import evaluate_public_key_form_Wallet
import scramble_transaction


def function(con:Connection, req:Request)->Dict[str,Any]:
    sender:int = req.json["sender"]
    receiver:int = req.json["receiver"]
    sender_signature:str = req.json["sender_signature"]
    amount:int = req.json["amount"]

    t:Transaction = Transaction(
        sender=sender,
        receiver=receiver,
        sender_signature=sender_signature,
        amount=amount
        )

    if does_wallet_exist_in_db.check(con, sender) == False:
        return {
            "is_ok":False,
            "exit_code":"SENDER_WALLET_DOES_NOT_EXIST",
        }

    address_check_exit_code:str = is_transaction_valid_by_address.check(con, t)
    if address_check_exit_code != "OK":
        return {
            "is_ok":False,
            "exit_code":address_check_exit_code,
        }

    amount_check_exit_code:str = is_tarnsaction_valid_by_amount.check(con, t)
    if  amount_check_exit_code != "OK":
        return {
            "is_ok":False,
            "exit_code":amount_check_exit_code,
        }

    #getting the wallet info
    wallet:Wallet = read_wallet_by_address_from_db.read(con, sender)

    #scambing the transaction
    scramble:bytes = scramble_transaction.scramble(t)

    #making signatuer usebale
    signature_bytearray:bytes = base64.b64decode(sender_signature.encode(encoding="ascii"))
    pub_key:PublicKey = evaluate_public_key_form_Wallet.evaluate(wallet)
    verification:bool = rsa.verify(scramble, signature_bytearray, pub_key)

    if verification == False:
        return {
            "is_ok":False,
            "exit_code":"SIGNATURE_INVALID",
        }







