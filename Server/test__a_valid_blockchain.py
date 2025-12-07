from typing import *

from rsa import PrivateKey

import leading_zero_generate_blockchain_for_test
import validate_blockchain
from Block import Block
from Wallet import Wallet


def main()->bool:
    block_chain:List[Block] = None
    wallets:List[Wallet] = None
    priv_keys:List[PrivateKey] = None
    block_chain, wallet, priv_key = leading_zero_generate_blockchain_for_test.generate(10)
    print(validate_blockchain.validate(block_chain, wallets))





if __name__ == "__main__":
    main()