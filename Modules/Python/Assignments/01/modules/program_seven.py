#!/bin/python

from modules.program import Program





class ProgramSeven(Program):
    _name="Calculate Total"
    _desc="Calcuate total based on quantity and price"
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)


    def run(self):
        price = float(self.read("Price? "))
        quantity = float(self.read("Quantity? "))


        # print the out
        
        self.echo(f"Report(UnitPrice=${price}, UnitCount={quantity}, TOTAL=${price * quantity})")
