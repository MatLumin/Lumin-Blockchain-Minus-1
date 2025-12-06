



from rsa import PrivateKey, PublicKey

from Wallet import Wallet
from Transaction import Transaction
import sign_transaction
import verify_tarnsction_signature
import generate_wallet_for_testing



def main()->bool:
    priv: PrivateKey
    w, priv = generate_wallet_for_testing.generatre(0)
    t: Transaction = Transaction(
        sender=0,
        receiver=1,
        sender_signature="NONE",
        amount=2,
    )
    singing_status:str = sign_transaction.sign(t, priv, w)
    return verify_tarnsction_signature.verify(t, w)





if __name__ == "__main__":

    print("signing and verification of transaction is done right?", main())