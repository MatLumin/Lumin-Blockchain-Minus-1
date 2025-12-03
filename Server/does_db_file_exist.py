

import os

import GLOBAL_CONST



def check()->bool:
    return os.path.exists(GLOBAL_CONST.DATABASE_FILE_NAME)

