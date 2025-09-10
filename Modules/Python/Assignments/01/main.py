#!/bin/python

import sys


from modules.program import Program
from modules.program_one import ProgramOne
from modules.program_two import ProgramTwo
from modules.program_three import ProgramThree
from modules.program_four import ProgramFour


from modules.program_five import ProgramFive

from modules.program_six import ProgramSix
from modules.program_seven import ProgramSeven


# programs
programs:list[Program] = [
    ProgramOne,
    ProgramTwo,
    ProgramThree,
    ProgramFour,
    ProgramFive,
    # ProgramSix,
    ProgramSeven,
]



# main
def main(pid:int=None):
    if pid == None:
        print("[A] Assignment Solution Started!\n")
        for index in range(0, len(programs)):
            ins = programs[index](id=index+1)
            ins.run()
            ins.end()
    else:
        ins = programs[pid-1](id=pid)
        ins.run()
        ins.end()



# run
if __name__ == "__main__":
    # try:
    if len(sys.argv) < 2:
        main()
    else:
        main(pid=int(sys.argv[1]))
    # except Exception as Error:
    #     print(Error)
    #     print("[!] Unexpected Error Happened.")
