

import hashlib



def hash(value:bytes)->bytes:
    return hashlib.sha256(value).digest()



if __name__ == "__main__":
    print(hash("HELLO".encode(encoding="ascii")))