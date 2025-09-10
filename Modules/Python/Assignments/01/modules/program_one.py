#!/bin/python


from modules.program import Program


"""doc
    we will write the program description here
"""

class ProgramOne(Program):
    _name = "Hello, World!"
    _desc = "Just printing 'Hello, World!' sentense."
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)
        

    def run(self):
        # COMMENT: This code prints "Hello, World!"
        self.echo("Hello, World")
