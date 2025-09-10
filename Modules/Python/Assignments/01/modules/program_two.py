#!/bin/python



from modules.program import Program

class Person:
    _name:str
    _city:str
    _age:int
    def __init__(self, name, city, age):
        self._name = name.title()
        self._city = city.upper()
        self._age  = int(age)



    def toString(self):
        return f"Person(name={self._name}, city={self._city}, age={self._age})"

        
class ProgramTwo(Program):
    _name = "Print Personal Info"
    _desc = "Just take Person Info and print them"
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)




    def run(self):
        person = Person(
            name=self.read("Username? "),
            city=self.read("City? "),
            age=self.read("Age? "),
        )


        self.echo(person.toString())
        
