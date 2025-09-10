#!/bin/python

# this is a program classs

# Packages
from modules.constants import INDENT_SIZE

# Program
class Program:
    _indent:str = f"{' ' * INDENT_SIZE}"
    _id:int
    _name:str
    _desc:str
    def __init__(self, id:int, name:str, desc:str=""):
        self._id = id
        self._name = name.title()
        self._desc = desc


        # Printing Program Header when run it
        self.header()
    
    def header(self):
        print(f"[{self._id}] {self._name}")
        
    def echo(self, text, flag="+", plain=False):
        if plain:
            print(text)
        else:
            print(f"{self._indent}{text}")

    def read(self, label):
        value = input(f"{self._indent}{label}")
        return value
        
    def run(self):
        pass

    def end(self):
        self.echo(" *", plain=True)
        print()
