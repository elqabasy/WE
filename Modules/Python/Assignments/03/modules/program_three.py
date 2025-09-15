#!/bin/python


from dataclasses import dataclass

from modules.program import Program



@dataclass
class Range:
    start:int
    end:int

@dataclass
class Error:
    code:str
    name:str
    details:str

@dataclass
class Result:
    ok:True
    error:Error=None
    value:object=None


class ProgramThree(Program):
    _name = "Even Numbers Between Range"
    _desc = ""
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)

    
    def readRange(self)->Result:
        
        start, end = [val.strip(" ,") for val in self.read("Range? ").strip(" ,").split(",")]
        

        if start in [None, "", " "]:
            return Result(ok=False, error=Error(name="Incorrect start value!"))

        if end in [None, "", " "]:
            return Result(ok=False, error=Error(name="Incorrect end value!"))


        # auto make it in correct order,
        # smaller, greater like 0, 20
        start, end = [int(start), int(end)]
        start, end = [min(start, end), max(start, end)]
        
        return Result(ok=True, value=Range(start, end))


    def isEven(self, n:int):
        return n % 2 == 0
    
    def isOdd(self, n:int):
        return not self.isEven(n)


    """doc
        - this is a very powerfull code,
        - it prins the evens in a specific range 
            Without any Looop
    """
    def print_evens(self, rng:Range):
        rng_list = range(
            rng.start if self.isEven(rng.start) else rng.start+1, 
            rng.end+1 if self.isEven(rng.end) else rng.end, 2
        )
        self.echo("Evens: {rng}".format(rng=', '.join([str(x) for x in rng_list])))
    
    def help(self):
        self.echo("Format(start, end): n1, n2")

    def run(self):
        self.help()
        result = self.readRange()
        if result.ok:
            self.print_evens(result.value)
        # self.echo("PROGRAM THREE")