import base64
from typing import *
import time
import random

from rsa import PrivateKey

import hash_block
import leading_zero_solver
import GLOBAL_CONST
import get_all_wallet_balance_without_db
from Block import Block
import turn_bytes_to_base64_string
import get_keys_of_dict
from Wallet import Wallet
import generate_all_possible_wallets_for_test_purpose
import sign_transaction


def generate(length:int, difficulty:int)->List[Block]:
    output:List[Block] = []


    list_of_all_wallet_addresses:List[int] = list(range(0, GLOBAL_CONST.MAX_WALLET_COUNT))
    print("list_of_all_wallet_addresses", list_of_all_wallet_addresses)
    input("press enter")
    premortal_balance:int = GLOBAL_CONST.MAX_COIN_COUNT


    #first transfer initial balance of the wallets from premortal wallet
    previous_hash:str=None
    while True:
        print(premortal_balance)
        if premortal_balance == 0:
            break
        #first pick a random wallet address
        random_wallet_address:int = random.choice(list_of_all_wallet_addresses)
        rwa:int=random_wallet_address

        #amount to transfer

        #now decrement a random amount from the money it must be in it
        premortal_balance -= GLOBAL_CONST.PREMORTAL_MINING_REWARD


        previous_hash:str = "0"
        if len(output) != 0:
            previous_hash = base64.b64encode(hash_block.hash(output[-1])).decode(encoding="ascii")


        b = Block(
            amount=GLOBAL_CONST.PREMORTAL_MINING_REWARD,
            sender=GLOBAL_CONST.PREMORTAL_WALLET_ADDRES,
            receiver=rwa,
            sender_signature="FAKE_SIGNATURE_FOR_TEST_PURPOSE_SIR_SO_DONT_BE_A_BRATTY_SLUT",
            previous_hash=previous_hash,
            index=len(output),
            unix=time.time_ns(),
            nonce="NONE",
            pow_algho_name="LEADING_ZERO",
            pow_algho_difficulty=GLOBAL_CONST.NORMAL_TRANSACTION_DIFFICULTY,
        )
        leading_zero_solver.solve(b)
        output.append(b)


    all_wallets:List[Wallet] = None
    wallets_priv_key:List[PrivateKey] = None
    all_wallets, wallets_priv_key = generate_all_possible_wallets_for_test_purpose.generatre()


    i:int
    for i in range(0, length):

        balance:Dict[int,int] = get_all_wallet_balance_without_db.get(output)


        #pick a random sender
        sender:int = random.choice(get_keys_of_dict.get(balance))
        print("sender",sender)
        #pick a random receiver
        receiver:int = None
        while (receiver is None)==False and receiver != sender:
            receiver = random.choice(list_of_all_wallet_addresses)

        #random amount from sender's networth
        amount:int = random.randint(0,balance[sender])

        b:Block = Block(
            amount=amount,
            sender=sender,
            receiver=receiver,
            sender_signature="FAKE_SIGNATURE_FOR_TEST_PURPOSE_SIR_SO_DONT_BE_A_BRATTY_SLUT",
            previous_hash=base64.b64encode(hash_block.hash(output[-1])).decode(encoding="ascii"),
            index=len(output),
            unix=time.time_ns(),
            nonce="NONE",
            pow_algho_name="LEADING_ZERO",
            pow_algho_difficulty=GLOBAL_CONST.NORMAL_TRANSACTION_DIFFICULTY,
        )

        leading_zero_solver.solve(b)
        output.append(b)




    return output


if __name__ == "__main__":
    print(generate(10, 5))



