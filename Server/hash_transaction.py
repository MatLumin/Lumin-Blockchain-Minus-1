

import hash as hasher
import scramble_transaction
from Transaction import Transaction

def hash(t:Transaction)->bytes:
    return hasher.hash(scramble_transaction.scramble(t))



if __name__ == '__main__':
    t:Transaction = Transaction(
        sender=0,
        receiver=1,
        sender_signature="ABCDEFG",
        amount=1,
    )
    print(hash(t))