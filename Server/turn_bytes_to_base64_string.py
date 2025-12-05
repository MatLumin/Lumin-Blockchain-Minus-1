
import base64





def turn(b:bytes)->str:
    return base64.b64encode(b).decode(encoding="ascii")