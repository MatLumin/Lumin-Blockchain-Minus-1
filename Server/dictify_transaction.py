from typing import *

from Transaction import Transaction




def dictify(t:Transaction)->Dict[str,Any]:
    return {
        "sender":t.sender,
        "receiver":t.receiver,
        "sender_signature":t.sender_signature,
        "amount":t.amount,
    }