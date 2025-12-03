import sys

import requests
from requests import Response

import config
from Transaction import Transaction
import sign_transaction

HELP_TEXT:str = """
make a transaction, takes two arguments
first is the address of receiver
second is the amount

#not this code wont check for errors
#server will smack you in face if you give it invalid, garbage values
"""


def main()->None:
    receiver:int = int(sys.argv[1])
    amount:int = int(sys.argv[2])
    t:Transaction = Transaction(
        sender=config.SELF_WALLET_ADDRESS,
        receiver=receiver,
        amount=amount,
        sender_signature="NONE"
    )
    signature:str = sign_transaction.sign(t)
    print(signature)
    res:Response = requests.post(
        config.ROUTER_ADDRESS+"/make_transaction",
        json={
            "sender": config.SELF_WALLET_ADDRESS,
            "receiver": receiver,
            "sender_signature": signature,
            "amount": amount,
        }
    )
    print(res.text)
    return None





if __name__=="__main__":
    main()