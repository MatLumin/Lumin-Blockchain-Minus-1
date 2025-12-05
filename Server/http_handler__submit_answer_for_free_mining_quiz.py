from typing import *

from flask.wrappers import Request

from Quiz import Quiz
import validate_leading_zero_quiz





def function(free_mining_quizes:Dict[int,Quiz], req:Request)->Dict[str,Any]:

    if "answer" not in req.json:
        return {
            "is_ok":False,
            "exit_code":"ANSWER_IS_MISSING"
        }

    answer:int = req.json["answer"]


    if "look_up_id" not in req.json:
        return {
            "is_ok":False,
            "exit_code":"LOOK_UP_ID_IS_MISSING"
        }

    look_up_id:int = req.json["look_up_id"]

    #first check if quiz if such quiz even exist
    if (look_up_id in free_mining_quizes) == False:
        return {
            "is_ok":False,
            "exit_code":"NO_SUCH_QUIZ_EXIST"
        }


    quiz:Quiz = free_mining_quizes[look_up_id]

    #cheki if given answer is valid
    validation_result:bool = validate_leading_zero_quiz.validate(quiz, answer)

    if validation_result == False:
        return {
            "is_ok":False,
            "exit_code":"ANSWER_IS_WRONG"
        }
