from typing import *




def join(a:Dict[Any,Any], b:Dict[Any,Any])->Dict[Any,Any]:
    output:Dict[Any,Any] = a.copy()
    output.update(b)
    return output