

from dataclasses import dataclass
from utils.structs.error import Error

@dataclass
class BinarySearchResult:
    ok:bool
    value:object
    error:Error