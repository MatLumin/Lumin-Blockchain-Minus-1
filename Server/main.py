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

threads:List[Thread] = []


app:Flask = Flask(__name__)
DB_CONNECTION:sqlite3.Connection = sqlite3.connect(GLOBAL_CONST.DATABASE_FILE_NAME, check_same_thread=False)





def tkinter_thread_function()->None:
    root:tkinter.Tk= tkinter.Tk()
    root.geometry("600x600")
    root.title("lUMIN BLOCK CHAIN")
    STATS_LABEL:tkinter.Label = tkinter.Label(root, text="STATS")
    STATS_LABEL.pack()

    root.mainloop()


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




if __name__ == '__main__':

    if does_db_file_exist.check() == False:
        make_db_file.make()
        define_Block_in_db_file.define()
        define_Wallet_in_db.define()

    #flask_thread:Thread = Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8080, "debug":True})
    #tkinter_thread:Thread = Thread(target=tkinter_thread_function)

    #threads.append(tkinter_thread)
    #threads.append(flask_thread)

    #flask_thread.start()
    #tkinter_thread.start()

    #flask_thread.join()
    #tkinter_thread.join()


    app.run(host="0.0.0.0", port=2323, debug=True)
