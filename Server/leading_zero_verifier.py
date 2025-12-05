from typing import *


from Block import Block
import hash_block



def verify(b:Block)->str:
    """
    EXIT CODES:
        POW_ALGHO_NAME_DOES_NOT_MATCH
        PASSED
        FAILED
    """

    if b.pow_algho_name != "LEADING_ZERO":
        return "POW_ALGHO_NAME_DOES_NOT_MATCH"
    hashed:int = hash_block.hash(block=b)
    i:int
    count:int = 0
    for i in hashed:
        count += i==0

    c:bool = count==b.pow_algho_difficulty
    if c == True:
        return "PASSED"
    if c == False:
        return "FAILED"
