#!/bin/python






from modules.program import Program



class ProgramOne(Program):
    _name = "Split String"
    _desc = "Take a string as input and print all it's chars"
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)


    def run(self):
        user_input:str = self.read("String? ")

        self.echo(' '.join([x for x in user_input]))