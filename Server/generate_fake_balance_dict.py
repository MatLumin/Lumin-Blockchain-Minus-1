from typing import *


import GLOBAL_CONST
import generate_shuffled_range
import random_decrement
import sum_dict_values


def generate()->Dict[int,int]:
    #the key is the adress of waellt
    #the value is the balance
    output:Dict[int,int]=dict()
    total_balance:int = GLOBAL_CONST.MAX_COIN_COUNT
    for i in generate_shuffled_range.generate(0, GLOBAL_CONST.MAX_WALLET_COUNT-1):
        balance:int = random_decrement.decrement(total_balance, 5)
        output[i] = balance
        total_balance -= balance
    return output


if __name__=='__main__':
    print(generate())
