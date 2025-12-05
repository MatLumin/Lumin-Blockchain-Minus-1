from typing import *

from flask.wrappers import Request

import generate_leading_zero_quiz
import generate_lookup_id_for_quiz
from Quiz import Quiz



def function(free_mining_quizes:Dict[int,Quiz], req:Request)->Dict[str,Any]:
    q:Quiz =  generate_leading_zero_quiz.generate()
    lookup_id:int = generate_lookup_id_for_quiz.generate()
    free_mining_quizes[lookup_id] = q
    return {
        "is_ok":True,
        "data":{
            "quiz":{
                "string": q.string,
                "difficulty": q.difficulty,
            },
        "look_up_id":lookup_id
        }
    }