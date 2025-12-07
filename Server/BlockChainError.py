from dataclasses import dataclass
from typing import *


@dataclass
class BlochChainError:
    title:str
    caption:str
    args:Dict[str,Any]