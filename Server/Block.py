from dataclasses import dataclass


@dataclass
class Block:
    amount:int #21bits
    sender:int #8bits
    receiver:int #8bits
    sender_signature:str #base64 encoded of sha256 and rsa
    previous_hash:str #base64 encoded sha256
    index:int
    unix:int
    nonce:str