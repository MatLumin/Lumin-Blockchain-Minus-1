


from dataclasses import dataclass




@dataclass
class Wallet:
    public_key_n:int
    public_key_e:int
    address:int #8bits unsigned