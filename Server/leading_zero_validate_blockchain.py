import base64

from typing import *

from Block import Block
import leading_zero_verifier
import hash_block



def validate(chain:List[Block])->str:
    #will chack nounce and previous has
    #will check for transactions validity
    chains_copy = chain.copy()
    chains_copy.reverse()
    last_previous_hash:str = None #note previous has is the base64 encoded string
    #for comparison of hases you have to do the steps below to the calculated hash
    #first turn it into base64 which gives you a bytea rray
    #then turn it into a string by ascii encoding
    for block in chains_copy:
        if last_previous_hash != None:
            current_hash:str = base64.b64encode(hash_block.hash(block)).encode(encoding="ascii")
        #first check the nounce
        nounce_verification:str = leading_zero_verifier.verify(block)
        if nounce_verification == "POW_ALGHO_NAME_DOES_NOT_MATCH":
            return "POW_ALGHO_NAME_DOES_NOT_MATCH"
        elif nounce_verification == "FAILED":
            return "FAILED"
        elif nounce_verification == "PASSED":
            pass
        last_previous_hash = block.previous_hash
