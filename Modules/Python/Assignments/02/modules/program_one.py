#!/bin/python


from modules.program import Program


"""doc
    we will write the program description here
"""

class ProgramOne(Program):
    _name = "Get Max Number"
    _desc = "Take three numbers and return the max number."
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)
    
    

    def max(self, a:int, b:int):
        return a if a > b else b

    def process(self):
        tuple_numbers:tuple[int] = (
            int(self.read("Number1? ")),
            int(self.read("Number2? ")),
            int(self.read("Number3? ")),
        )


        self.echo("MAX: {}".format(self.max(tuple_numbers[0], max(tuple_numbers[1], tuple_numbers[2]))))


    def run(self):
        try:
            self.process()
        except Exception as Error:
            self.tryAgain(lambda: self.run(), before=f"Unexpected error happend!")
