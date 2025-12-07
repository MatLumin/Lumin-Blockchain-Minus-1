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
from Transaction import Transaction
import generate_all_possible_wallets_for_test_purpose
import sign_transaction
import is_transaction_valid_by_address_without_db
import is_tarnsaction_valid_by_amount_without_db


def generate(length:int)->Tuple[List[Block], List[Wallet], List[PrivateKey]]:
    output:List[Block] = []


    list_of_all_wallet_addresses:List[int] = list(range(0, GLOBAL_CONST.MAX_WALLET_COUNT))
    print("list_of_all_wallet_addresses", list_of_all_wallet_addresses)
    premortal_balance:int = GLOBAL_CONST.MAX_COIN_COUNT


    #first transfer initial balance of the wallets from premortal wallet
    previous_hash:str=None
    while True:
        if premortal_balance < GLOBAL_CONST.PREMORTAL_MINING_REWARD:
            print("ooopsie")
            break

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
            sender_signature=".",
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
    wallets_priv_keys:List[PrivateKey] = None
    print("generating wallets and private keys")
    all_wallets, wallets_priv_key = generate_all_possible_wallets_for_test_purpose.generatre()
    print("done generating wallets and private keys")

    i:int
    for i in range(0, length):

        balances:Dict[int,int] = get_all_wallet_balance_without_db.get(output)

        #pick a sender
        sender:int = None
        while sender is None:
            candidate_for_sending:int = random.choice(list_of_all_wallet_addresses)
            print("candidate_for_sending",candidate_for_sending)
            #first chek it has the minimum credit
            balance:Union[int,None] = balances.get(candidate_for_sending)
            if balance is None: #no freaking balance da
                continue

            if balance < (GLOBAL_CONST.NORMAL_TRANSACTION_FEE + 1):
                continue #it does not have the minimum networth

            sender = candidate_for_sending


        #getting the wallet lol
        sender_wallet:Wallet = None
        i:Wallet
        for i in all_wallets:
            if i.address == sender:
                sender_wallet = i


        #finding a receiver
        receiver:int = None
        while receiver is None:
            candidate_for_receiving:int = random.choice(list_of_all_wallet_addresses)
            print("candidate_for_receiving", candidate_for_receiving)
            if candidate_for_receiving == sender:
                #sender rend creciver are the same
                continue

            #nothing else to check tho
            receiver = candidate_for_receiving


        print(f"""
        sender:{sender}
        sender_walelt:{sender_wallet}
        receiver:{receiver}
        """)



        #random amount from sender's networth
        amount:int = random.randint(1,balances[sender])
        balances[sender] -= amount

        print("forming the transaction")
        t:Transaction = Transaction(
            sender=sender,
            receiver=receiver,
            sender_signature="TO_BE_SIGNED",
            amount=amount,
        )
        print("done forming the transaction")

        print("signing the transaction")
        sign_transaction.sign(
            t=t,
            private_key=wallets_priv_key[sender],
            wallet_of_sender=sender_wallet,
        )
        print("done signing the transaction")

        print("now checking the created transaction")
        is_valid_by_address:str = is_transaction_valid_by_address_without_db.check(t)
        is_valid_by_amount:str = is_tarnsaction_valid_by_amount_without_db.check(balances[sender], t)

        print("transaction", t)

        print("is_valid_by_address",is_valid_by_address)
        print("is_valid_by_amount",is_valid_by_amount)


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




    return (output, all_wallets, wallets_priv_keys)


if __name__ == "__main__":
    print(generate(10, 5))



