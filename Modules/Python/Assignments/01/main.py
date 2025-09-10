#!/bin/python


from modules.program import Program
from modules.program_one import ProgramOne
from modules.program_two import ProgramTwo
from modules.program_three import ProgramThree
from modules.program_four import ProgramFour
from modules.program_seven import ProgramSeven

programs:list[Program] = [
    # ProgramOne,
    # ProgramTwo,
    # ProgramThree,
    # ProgramFour,
    ProgramSeven,
]



# main
def main():
    print("[A] Assignment Solution Started!\n")

    
    for index in range(0, len(programs)):
        ins = programs[index](index+1)
        ins.run()
        ins.end()

# run
if __name__ == "__main__":
    main()
