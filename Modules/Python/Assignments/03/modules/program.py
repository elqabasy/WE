#!/bin/python

# this is a program classs

# Packages
from modules.constants import INDENT_SIZE, ERROR_MESSAGE


import getpass

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


    def tryAgain(self, func, before:str=ERROR_MESSAGE, after:str=None):
        if before != None:
            self.echo(before)

        again = self.read("Try agin? ").strip().lower()

        if again in ["y", "yes", "ok", "please"]:
            func()


        if after != None:
            self.echo(after)

    def id(self):
        return self._id

    def name(self):
        return self._name

    def desc(self):
        return self._desc
        
    def header(self):
        print(f"[{self._id}] {self._name}")
        
    def echo(self, text, flag="+", plain=False, re:object=None):
        if plain:
            print(text)
        else:
            print(f"{self._indent}{text}")
        return None
    
    def read(self, label, hidden:bool=False):
        label = f"{self._indent}{label}"
        if hidden:
            return getpass.getpass(label)
    
        return input(label)
        
    def run(self):
        pass

    def end(self):
        self.echo(" *", plain=True)
        print()
