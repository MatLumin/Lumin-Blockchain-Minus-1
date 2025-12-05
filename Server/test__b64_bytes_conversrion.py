import turn_bytes_to_base64_string
import turn_base64_string_to_bytes


def main()->bool:
    test:bytes = b"LUMIN"
    return test == turn_base64_string_to_bytes.turn(turn_bytes_to_base64_string.turn(test))



if __name__ == "__main__":
    print("was test ok?", main())