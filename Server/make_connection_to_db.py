


import sqlite3
from sqlite3 import Connection
import GLOBAL_CONST



def make()->Connection:
    return sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)