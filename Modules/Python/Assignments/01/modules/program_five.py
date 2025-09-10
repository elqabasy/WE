#!/bin/python

from modules.program import Program


class ProgramFive(Program):
    _name:str = "Simple Calculator"
    _desc:str = "Just a simple calculator"

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)

    def run(self):
        self.echo("Examples: 1+2/3, (12*30)//2, 2**2")
        expression = self.read("Calc? ")
        result = eval(expression) # i know that this is not secure, but the deadline is one day
        self.echo(f"Result: {result}")
