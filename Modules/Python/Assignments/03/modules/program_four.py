#!/bin/python

from dataclasses import dataclass

import random
from modules.program import Program
from utils.structs import Error, BinarySearchResult



class ProgramFour(Program):
    _name:str = "Find value from a list"
    _desc:str = ""
    dummy:list[int] = sorted([random.randint(0, 155) for x in range(0, 15)])

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)


    def bCenter(self, l, r):
        return int((l + r) / 2)


    def bSearch(self, target, array, l, r) -> int:
        center = self.bCenter(l, r)
        
        if l >= r :
            return -1
        
        if array[center] == target:
            return center 
        
        if target > array[center]:
            self.bSearch(target, array, center+1, r)
        else:
            self.bSearch(target, array, l, center-1)
        return 0


    def binarySearch(self, target, data):
        return self.bSearch(target, data, 0, len(data)-1)
    

    def help(self):
        self.echo("DummyList: {}".format(', '.join([str(x) for x in self.dummy])))

    
    def run(self):
        self.help()


        svalue = self.read("Search? ").strip()
        
        result = self.binarySearch(int(svalue), self.dummy)

        print(result)
        # if result == -1:
        #     self.echo("{value} is not found!".format(value=svalue))
        # else:
        #     self.echo("{value} is exists at {index}".format(value=svalue, index=result))


        # self.echo
        # print(x)
        # self.echo("PROGRAM_FOUR")