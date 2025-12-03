import requests
from requests import Response

import config


HELP_TEXT:str = "makes wallet"


def main()->None:
    res:Response = requests.get(config.ROUTER_ADDRESS+"/make_wallet")
    print(res.text)
    return None




if __name__ == "__main__":
    main()