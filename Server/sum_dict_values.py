from typing import *



def sum(a:Dict[Any,int])->int:
    output = 0
    for k,v in a.items():
        output += v
    return output