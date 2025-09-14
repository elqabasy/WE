#!/bin/python


from dataclasses import dataclass

from modules.program import Program
from modules.dummy import menu_data


"""doc
    - what we need is a nested menu component, that we 
        can choose from it like this:
        1.2 - this is category one, item two
    

    - so, we have data:
        many data
            many categories
                many itmes

                

    
"""


@dataclass
class Item:
    name:str
    price:str
    category:str

class DB:
    _rows:dict[str, dict[str, float]] = menu_data.ROWS

    def __init__(self):
        pass

    
    def byCategory(self, name:str, limit=None)->list[Item]:
        name = name.strip().lower()
        result = []
        if name != "" and name in self._rows.keys():
            result = [Item(category=name, price=self._rows[name][key], name=key) for key in self._rows[name]]

        if type(limit) is int and limit >= 0:
            return result[:limit]

        return result
    


    def all(self, limit=None)->list[Item]:
        result = [[Item(
            name=item, price=self._rows[key][item], category=key
        ) for item in self._rows[key]] for key in self._rows]

        if limit != None and limit >= 0:
            return result[:limit]
        
        return result


    # def byIndex(self, index:int, limit=None)->Item:
@dataclass
class Option:
    cname:str
    iname:str

class Menu:
    """doc
        - this is just an interface for accessing items in categories
    """ 
    db:DB
    def __init__(self, db:DB, echo=None, read=None):
        self.db = db
        self._echo = echo
        self._read = read
    
    def echo(self, text:str):
        self._echo(text)

    def read(self, label:str):
        self._read(label)

    def display(self):
        indent="  "
        data:list[list[Item]] = self.db.all()
        for i, row in enumerate(data, 1):
            self.echo("{i}. [{cn}]".format(cn=row[0].category, i=i))
            for index, item in enumerate(row, 0):
                self.echo("{indent}{id}. {name}, ${price}".format(indent=indent, id=index+1, name=item.name, price=item.price))

            self.echo("  .")


    def input(self, onSelect, onError):
        self.echo("Help: you can enter 2.1 or 1.1 and so on")
        value:str = self.read("Select Option? ")

        re = value.split(".")

        if len(re) == 1:
            onError("Incomplete choice!")
        else:
            cname = self.db._rows.keys()[int(re[0])-1]
            iname = self.db._rows[cname].keys()[int(re[1])-1]
            onSelect(Option(cname, iname))

    def run(self):
        self.display()
        self.input()

    
    


class ProgramFour(Program):
    _name = "A Restaurant menu management app"
    _desc = "Just same as name"

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)


    def run(self):
        # self.echo("Restaurant Menu")
        menu = Menu(DB(), self.echo, self.read)
        menu.run()