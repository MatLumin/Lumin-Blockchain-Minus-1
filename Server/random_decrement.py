import random

import GLOBAL_CONST


def decrement(value:int, max_precentage:int=100)->int:
    max_value:int = int(value/100 * max_precentage)
    return random.randint(0,max_value)