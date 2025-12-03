



import hash as hasher
import scramble_block
from Block import Block



def hash(block:Block)->bytes:
    return hasher.hash(scramble_block.scramble(block))


if __name__ == "__main__":
    b:Block = Block(
        amount=1,
        sender=0,
        receiver=0,
        sender_signature="ABCD",
        previous_hash="0",
        index=0,
        unix=0,
        nonce=0,
    )
    print(hash(b))