#!/bin/python

from enum import Enum
from modules.program import Program
from modules.constants import FLOATING_POINTS


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
        # the base is mm, millie meter
        'mm':1,
        'cm':10,
        'meter':1000,
        'km':1000*1000,
        'feet':0.3048*1000,
        'inch':0.0254*1000,
        'miles':1609.34*1000,
    }
    

    def __init__(self, value:float, unit:Unit):
        self._value = value
        self._unit = unit.lower()


    def unit(self):
        return self._unit


    def value(self):
        return self._value


    def toBase(self)->float:
        # convert this vlaue to base(mm)
        return float(self._all[self._unit] * self._value)
         

    def to(self, dest:Unit):
        base = self.toBase()
        converted:float = base / self._all[dest]
        return Distance(converted, dest)


    def toString(self):
        value = f"{self._value:,.{FLOATING_POINTS}f}"
        svalue = f"{self._value:,.0f}"
        return "Distance({2}{1}, value={0}, unit={1})".format(value, self._unit.upper(), svalue)



class ProgramFour(Program):
    _name:str = "Distance Converter"
    _desc:str = "Convert any distance.unit to any distance unit"

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)



    def run(self):
        units =  sorted(Distance._all, key=Distance._all.get)
        self.echo(f"Units: {', '.join(units)}")

        source = Distance(
            value=float(self.read("Source Value? ")), 
            unit=self.read("Source Unit? ")
        )

        dest = self.read("Dest Unit? ")



        self.echo("")
        
        result = source.to(dest)
        self.echo(result.toString())

        
