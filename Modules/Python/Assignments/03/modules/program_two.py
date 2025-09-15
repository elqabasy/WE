#!/bin/python



from modules.program import Program



class ProgramTwo(Program):
    _name = "Even or Odd"
    _desc = "Give me a list of number and i will categorize them based on even or odd"

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)

    def isEven(self, n:int) -> bool:
        return n % 2 == 0
    
    def isOdd(self, n:int)-> bool:
        return not self.isEven(n)
    
    def help(self):
        self.echo("Format: n1, n2, n3, ..")


    def categorize(self, input_list:str):
        user_input = input_list.strip(" ,").split(",")
        categories = {"odd":[], "even":[]}
        
        for n in user_input:
            n = n.strip(" ,")
            if n in [None, " ", ""]:
                continue

            n = int(n)
            if self.isOdd(n):
                categories["odd"].append(n)
            else:
                categories["even"].append(n)    
        
        return categories
    

    def print(self, categories):
        for key in categories:
            self.echo("{key}: {values}".format(key=str(key).title(), values=', '.join([str(x) for x in categories[key]])))

    def run(self):
        self.help()
        self.print(self.categorize(self.read("Numbers? ")))





