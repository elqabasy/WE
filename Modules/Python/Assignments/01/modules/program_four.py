#!/bin/python

from enum import Enum
from modules.program import Program



class Unit(Enum):
    CM      = "cm"
    KM      = "km"
    FEET    = "feet"
    INCH    = "inch"
    METER   = "meter"
    MILES   = "miles"
    MM      = "mm"




class Distance:
    _value:float
    _unit:Unit

    _all = {
        # the base is cm
        'cm':1,
        'mm':0.1,
        'meter':100,
        'km':1000*100,
        'feet':0.3048*100,
        'inch':0.0254*100,
        'miles':1609.34*100,
    }

    def __init__(self, value:float, unit:Unit):
        self._value = value
        self._unit = unit


    def unit(self):
        return self._unit


    def value(self):
        return self._value


    def isDivision(self, source:Unit, dest:Unit):
        source = source.value if type(source) is Unit else source
        dest = dest.value if type(dest) is Unit else dest
        
        # km to meter
        if self._all[source] > self._all[dest]:
            return False # is multiplication

        return True

    def isMultiplication(self, source:Unit, dest:Unit):
        return not self.isDivision(source, dest)
        

    def to(self, dest:Unit):
        dest = dest.value if type(dest) is Unit else dest
        source = self._unit
        converted:float = self.value() * float(self._all[dest]) if self.isMultiplication(source,dest) else self.value() / float(self._all[dest])
        return Distance(converted, dest)


    def toString(self):
        return f"Distance(value={self._value}, unit={self._unit})"







class ProgramFour(Program):
    _name:str = "Distance Converter"
    _desc:str = "Convert any distance.unit to any distance unit"

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)



    def run(self):
        self.echo(f"Units: {', '.join(Distance._all.keys())}")

        source = Distance(
            value=float(self.read("Source Value? ")), 
            unit=self.read("Source Unit? ")
        )

        dest = self.read("Dest Unit? ")


        result = source.to(dest)
        self.echo(result.toString())

        # stopped here
        self.echo("I WILL CONTINUE LATER")    
            # self.echo("Success")
        # d = Distance(10, Unit.CM)
        # self.echo(d.toString())
        # self.echo(d.to(Unit.METER).toString())
