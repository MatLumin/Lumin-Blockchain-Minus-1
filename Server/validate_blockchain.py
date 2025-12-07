from typing import *

from Block import Block
from Wallet import Wallet
from BlockChainError import BlochChainError
import GLOBAL_CONST
import get_all_wallet_balance_without_db
import obtain_transaction_object_from_block
import is_transaction_valid_by_address_without_db
import is_tarnsaction_valid_by_amount_without_db
import dictify_transaction
import join_dicts

#fuck ya


def validate(block_chain:List[Block], wallets:List[Wallet])->List[BlochChainError]:
    errors:List[BlochChainError] = []
    #first step is to see the balance of wallets extracted from the blockchain
    balances:Dict[int, int] = get_all_wallet_balance_without_db.get(block_chain)

    #sum of all wallets, balance must not go above the total coin count
    sum_of_all_balance:int = 0#note the balance of premortal wallet is not included here
    for wallet_address, balance in balances.items():
        if wallet_address == GLOBAL_CONST.PREMORTAL_WALLET_ADDRES:
            continue
        sum_of_all_balance += balance

    print("balances",balances)
    if (sum_of_all_balance <= GLOBAL_CONST.MAX_COIN_COUNT) == False:
        errors.append(BlochChainError(
            title="SUM_OF_BALANCES_EXCEEDS_MAX_COIN_COINT",
            caption="title explains it",
            args={"sum_of_all_balance":sum_of_all_balance, "max_coin_count":GLOBAL_CONST.MAX_COIN_COUNT},
        ))

    #the amount that was transited from premortal wallet must not exceed the total coin count
    #in other words -> Balance_of_premortal_wallet+sum_of_all_balance=0
    if (balances[GLOBAL_CONST.PREMORTAL_WALLET_ADDRES]+sum_of_all_balance!=0):
        errors.append(BlochChainError(
            title="ADDITION_OF_PREMORTAL_BALANCE_AND_SUM_OF_ALL_WALLETS_BALANCE_IS_NOT_ZERO",
            caption="title explains it",
            args={"pre_mortal_wallet_balance": balances[GLOBAL_CONST.PREMORTAL_WALLET_ADDRES], "sum_of_all_balance": sum_of_all_balance},
        ))



    #also the value withdrawn from premortal wallet must not exceed the max coin count
    #note the balance of premortal wallet is negetice due to the fact no money comes to it
    if -1*balances[GLOBAL_CONST.PREMORTAL_WALLET_ADDRES] > GLOBAL_CONST.MAX_COIN_COUNT:
        errors.append(BlochChainError(
            title="MONEY_WIDRAWN_FROM_PREMORTAL_WALLET_EXCEEDS_MAX_COIN_COUNT",
            caption="title explains it",
            args={
                "absolute_pre_mortal_wallet_balance": abs(balances[GLOBAL_CONST.PREMORTAL_WALLET_ADDRES]),
                "max_coin_count": GLOBAL_CONST.MAX_COIN_COUNT
            },
        ))


    #now obtain transaction from all of the blocks and verify them all
    b:Block
    for b in block_chain:
        t:Transaction = obtain_transaction_object_from_block.obtain(b)
        exit_code:str = is_transaction_valid_by_address_without_db.check(t)
        if exit_code !="OK":
            errors.append(BlochChainError(
                title=exit_code,
                caption="title explains it",
                args=dictify_transaction.dictify(t)
            ))
        exit_code:str = is_tarnsaction_valid_by_amount_without_db.check(wallet_balance=balances[t.sender],transaction=t,)
        if exit_code !="OK":
            errors.append(BlochChainError(
                title=exit_code,
                caption="title explains it",
                args=join_dicts.join(dictify_transaction.dictify(t), {"sender_balance":balances[t.sender]})
            ))




    return errors



