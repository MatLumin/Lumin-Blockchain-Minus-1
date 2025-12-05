

from typing import *

from Block import Block



def get(blocks:List[Block])->Dict[int,int]:
    #in output key is the address of wallet and the value is the balance
    #note this function does not care about validity of blocks!
    output:Dict[int,int] = dict()
    for block in blocks:
        if (block.sender in output)==False:
            output[block.sender] = 0
        if (block.receiver in output)==False:
            output[block.receiver] = 0


        output[block.sender] -= block.amount
        output[block.receiver] += block.amount

    return output
