#!/bin/python

import sys


from modules.program import Program
from modules.program_one import ProgramOne
from modules.program_two import ProgramTwo
from modules.program_three import ProgramThree




# programs
programs:list[Program] = [
    ProgramOne,
    ProgramTwo,
    ProgramThree,
]



# main
def main(pid:int=None):
    if pid == None:
        print("[B] Assignment Solution Started!\n")
        for index in range(0, len(programs)):
            ins = programs[index](id=index+1)
            ins.run()
            ins.end()
    else:
        ins:Program = programs[pid-1](id=pid)
        ins.run()
        ins.end()





def tryAgin(func, before:str=None, after:str=None):
    if before != None:
        print(before)

        again = input("Try agin? ").strip().lower()

        if again in ["y", "yes", "ok", "please", "yea"]:
            try:
                func()
            except Exception as error:
                tryAgin(tryAgin, "An error has been occured!")

    if after != None:
        print(after)


# run
if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            main()
        else:
            main(pid=int(sys.argv[1]))

        print("Thank You for your TIME!")
        print("Developed with ❤️  by Mahros Al-Qabasy")
        input("Press <enter> to close!")
    except Exception as Error:
        tryAgin(main, Error)
        
