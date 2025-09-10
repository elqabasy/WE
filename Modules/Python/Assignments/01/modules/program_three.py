#!/bin/python


from modules.program import Program



class Draw:
    _rows:list[str]
    def __init__(self, rows:list[str]=[]):
        self._rows = rows

    def length(self):
        return len(self._rows) 

    def isEmpty(self):
        return self._rows <= 0

    def isNotEmpty(self):
        return not self.isEmpty()
        
    def rows(self):
        return self._rows

    def at(self, index)->str:
        if index >=0 and index < self.length():
            return _rows[index]

        return "IndexError: Index is out of range."

    def toString(self, indent=""):
        result=""

        for row in self.rows():
            result += f"{indent}{row}\n"

        return result    
        
    def append(self, value:str):
        self._rows.append(value)
    
    
class Rectangle:
    _length:int = 0
    _width:int  = 0
    def __init__(self, length:int, width:int):
        if length >= 0 and width >= 0:
            self._length = length
            self._width = width

    def area(self):
        # rec.area = length * width
        return self._length * self._width

    def toString(self):
        return f"Rectangle(length={self._length}, width={self._width}, area={self.area()})"

    def toDraw(self, fill='#', empty=' ',)-> Draw:
        l = self._length
        w = self._width

        draw:Draw = Draw() # empty for now


        for row in range(0, l):
            if row in [0, l-1]:
                draw.append(f"{fill * w*2}")
                continue

            draw.append(f"{fill}{empty * (w*2 - 2)}{fill}")


        return draw
        ######
        #    #
        #    #
        #    #
        #    #
        ######

        

        

class ProgramThree(Program):
    _name = "Calculate Rectangle Area"
    _desc = "Just Calculating Rectangle area and draw it"
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)




    def run(self):
        length = int(self.read("Length? "))
        width  = int(self.read("Width?  "))
        
        rec = Rectangle(length=length,width=width)

        # now we will print it to the screen
        
        self.echo(rec.toDraw().toString(indent=self._indent), plain=True)
        self.echo(rec.toString())
