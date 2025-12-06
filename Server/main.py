from typing import *
from threading import Thread
import tkinter
import sqlite3

from flask import Flask
import flask

import GLOBAL_CONST

#data base shit
import make_db_file
import does_db_file_exist
import define_Block_in_db_file
import define_Wallet_in_db
import make_connection_to_db



#http handlers
import http_handler__get_all_wallets_balance
import http_handler__get_all_blocks
import  http_handler__make_wallet
import http_handler__make_transaction
import http_handler__start_mining_quiz
import http_handler__submit_answer_for_free_mining_quiz
#structs
from Quiz import Quiz
import config













"""
@app.post("/start_free_mining_quizes")
def h4():
    return http_handler__start_mining_quiz.function(free_mining_quizes, flask.request)
"""

"""
@app.post("/submit_answer_for_free_mining_quiz")
def h5():
    return http_handler__submit_answer_for_free_mining_quiz.function(free_mining_quizes, flask.request)
"""



def construct_and_run_a_node_server():
    app: Flask = Flask(__name__)
    DB_CONNECTION: sqlite3.Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME, check_same_thread=False)
    free_mining_quizes: Dict[int, Quiz] = dict()


    @app.get("/get_all_wallets_balance")
    def h0():
        return http_handler__get_all_wallets_balance.function(DB_CONNECTION)



    @app.get("/get_all_blocks")
    def h1():
        return http_handler__get_all_blocks.function(DB_CONNECTION)


    @app.get("/make_wallet")
    def h2():
        return http_handler__make_wallet.function(DB_CONNECTION)


    @app.post("/make_transaction")
    def h3():
        return http_handler__make_transaction.function(DB_CONNECTION, flask.request)

    if does_db_file_exist.check() == False:
        make_db_file.make()
        define_Block_in_db_file.define()
        define_Wallet_in_db.define()

    app.run(host=config.SELF_HOST, port=config.SELF_PORT, debug=True)


if __name__ == '__main__':
    construct_and_run_a_node_server()









