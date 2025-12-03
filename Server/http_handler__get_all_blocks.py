from typing import *
from sqlite3 import Connection


from Block import Block
import read_all_Block_from_db


def function(con:Connection)->Dict[str,Any]:
    all_blocks:List[Block] = read_all_Block_from_db.read(con)
    output:Dict[int, Dict[str,Any]] = dict()

    b:Block
    for b in all_blocks:
        output[b.index] = {
            "amount":b.amount,
            "sender":b.sender,
            "receiver":b.receiver,
            "sender_signature":b.sender_signature,
            "previous_hash":b.previous_hash,
            "index":b.index,
            "unix":b.unix,
            "nonce":b.nonce,
        }

    return {
        "is_ok":True,
        "data":output
    }
