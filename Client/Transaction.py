




from dataclasses import dataclass



@dataclass
class Transaction:
    sender:int #8 bits
    receiver:int #8 bits
    sender_signature:str #base 64 rsa sha256
    amount:int