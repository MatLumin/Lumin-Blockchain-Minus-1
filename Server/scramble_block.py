from Block import Block


def scramble(block:Block)->bytes:
    p:str = ""
    p += str(block.amount)
    p += str(block.sender)
    p += str(block.receiver)
    p += str(block.sender_signature)
    p += str(block.previous_hash)
    p += str(block.index)
    p += str(block.unix)
    p += str(block.nonce)
    return p.encode(encoding="ascii")