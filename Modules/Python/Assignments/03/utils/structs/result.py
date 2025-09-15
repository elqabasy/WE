#!/bin/python




from dataclasses import dataclass
from typing import TypeVar


from .error import Error

T = TypeVar("T")
@dataclass
class Result:
    ok:bool
    value:T
    error:Error
