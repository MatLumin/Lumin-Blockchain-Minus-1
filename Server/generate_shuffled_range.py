from typing import *
import random







def generate(start, end)->List[int]:
    #start and end are inclusive!
    output = list(range(start, end+1))
    random.shuffle(output)
    return output
