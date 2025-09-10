#!/bin/python

""" some notes before we start coding

    Objects:
        - Book
        - Pen
        - and so on, so we can say: Item, for  generalization


        - Item:
            id, name, price, desc

        the lib. has many [Item]s
        those items exists in [Store]s
        any [Store] has multiple [Item]s
        also it may has many stores    
    
        Store:
            id, name, location, capacity


        
        also the lib has a [Vault], this contians the money
        the balance is zero, when we start for example

    by the END:
        I see that i have no time for this, 
        i will keep it simple for now
"""

class Item:
    _id:int
    _name:str
    _price:float
    _qty:int
    def __init__(self, id, name, price, qty):
        self._id    = id
        self._name  = name.title()
        self._price = price
        self._qty   = qty


    # getters
    def id(self):   
        return self._id
        
    def name(self):
        return self._name.title()

    def qty(self):
        return self._qty

    def price(self):
        return self._price

    def isEmpty(self):
        return self._qty <= 0

    def isNotEmpty(self):
        return not self.isEmpty()
        
    def toString(self):
        return f"Item(name={self.name()}, price={self.price()}, qty={self.qty()})"

    
class LibraryDB:
    _items:list[Item]
    
    def __init__(self, items=[], echo=None):
        self.echo = echo
        if len(items) > 0:
            self._items = items

    def isEmpty(self):
        return len(self._items) == 0

    def isNotEmpty(self):
        return not self.isEmpty()

    def length(self):
        return len(self._items)
        
    def display(self):
        if self.isNotEmpty():
            print(f"We have {self.length()} Items")
            for item in self._items:
                print(item.toString())

    # crud operations
    def getItem(self, id):
        # return self._items.
        pass
    
class Library:
    _db:LibraryDB
    def __init__(self, db:LibraryDB, echo=None):
        self._db    = db
        self.echo   = echo

    def run(self):
        self.echo("Running Library user interface")





from modules.program import Program

class ProgramSix(Program):
    _name = "Library System"
    _desc = "A system for a library management"
    def __init__(self, id):
        super().__init__(id, self._name, self._desc)





    def run(self):
        pass
        # self.echo("Success")
        db  = LibraryDB(echo=self.echo)
        lib = Library(db, echo=self.echo)
        lib.run()
        
