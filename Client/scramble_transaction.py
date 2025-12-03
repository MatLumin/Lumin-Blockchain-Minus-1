from Transaction import Transaction


def scramble(t:Transaction)->bytes:
    p:str = ""
    p += str(t.sender)
    p += str(t.receiver)
    #p += str(t.sender_signature)
    p += str(t.amount)
    return p.encode(encoding='ascii')

