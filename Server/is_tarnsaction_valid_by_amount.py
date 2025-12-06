from sqlite3 import Connection

from Transaction import Transaction

import GLOBAL_CONST
import get_balance_of_wallet
import is_tarnsaction_valid_by_amount_without_db


def check(con:Connection, transaction:Transaction)->str:
    return is_tarnsaction_valid_by_amount_without_db.check(
    get_balance_of_wallet.get(con, address=transaction.sender),
    transaction
    )

