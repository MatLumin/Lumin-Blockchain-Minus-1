from Transaction import Transaction
from Block import Block

def obtain(target:Block)->Transaction:
    return Transaction(
        sender=target.sender,
        receiver=target.receiver,
        sender_signature=target.sender_signature,
        amount=target.amount,
    )