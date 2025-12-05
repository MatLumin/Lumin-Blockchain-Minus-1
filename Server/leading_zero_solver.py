import time


from Block import Block
import leading_zero_verifier




def solve(block:Block)->str:
    #output will be the exit code
    #offred block my not be at use anywhere else
    if block.pow_algho_name != "LEADING_ZERO":
        return "POW_ALGHO_NAME_DOES_NOT_MATCH"
    start_time:float = time.time()
    answer:int = 0
    while True:
        block.nonce = str(answer)
        if leading_zero_verifier.verify(block) == "PASSED":
            break
        answer += 1
    print(time.time()-start_time, "time took to solve block:")
    return "OK"




if __name__ == "__main__":
    b:Block = Block(
        amount=2,
        sender=0,
        receiver=1,
        sender_signature="HELLO",
        previous_hash="0",
        index=0,
        unix=0,
        nonce="0",
        pow_algho_name="LEADING_ZERO",
        pow_algho_difficulty=5,
    )
    solve(b)