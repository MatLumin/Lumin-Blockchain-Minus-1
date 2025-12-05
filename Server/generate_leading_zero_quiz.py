import random


from Quiz import Quiz
import GLOBAL_CONST

def generate()->Quiz:
    string:str = ""

    for i in range(0, GLOBAL_CONST.QUIZ_STRING_LENGTH):
        string += chr(random.randint(33, 127))

    q = Quiz(
        string=string,
        difficulty=GLOBAL_CONST.QUIZ_DIFFICULTY,
    )

    return q



if __name__ == '__main__':
    print(generate())