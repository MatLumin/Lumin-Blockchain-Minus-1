
import requests
from requests import Response

import config

HELP_TEXT:str = "get all blocks"


def main()->None:
    res:Response = requests.get(config.ROUTER_ADDRESS+"/get_all_blocks")
    print(res.text.replace(",", ",\n"))
    return None



if __name__ == "__main__":
    main()