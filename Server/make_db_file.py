
import sqlite3
from sqlite3 import Connection
import GLOBAL_CONST


def make()->None:
    connection:Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME)
    connection.close()
    return 0