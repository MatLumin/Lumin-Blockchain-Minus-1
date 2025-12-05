
import base64




def turn(s:str)->bytes:
    return base64.b64decode(s.encode(encoding="ascii"))