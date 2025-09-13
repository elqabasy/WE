#!/bin/python


from modules.program import Program


class ProgramThree(Program):
    _name = "Print The Day of Week"
    _desc = "I will give you 1:7 and return the day of the week"

    def __init__(self, id):
        super().__init__(id, self._name, self._desc)





    def getDay(self, day):
        week = "Sa Su Mo Tu We Th Fr"
        try:
            day = int(day)
        except Exception as error:
            return self.echo("Day must be integer between 1..7!")


        if day >= 1 and day <= 7:
            return week.split(" ")[day-1]
        
        
        return self.echo("Incorrect day")

    def process(self):
        self.echo(f"Avi: {', '.join([str(x) for x in range(1,8)])}")

        id = self.read("Day? ")

        result = self.getDay(id)

        if result != None:
            self.echo("Result(id={}, day={})".format(id, result))
            return
        
        raise Exception("Try agin!")


    def run(self):
        try:
            self.process()
        except Exception as Error:
            self.tryAgain(self.process)