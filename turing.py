""" turing.py """

def terminates(program, inputData):
    # program and inputData are both strings
    # Returns true if program would halt when run with inputData
    # as its input.

def main():
    # Read a program from standard input
    lines = []
    print("Type in a program (type 'done' to quit). ")
    line = input("")
    while line != "done":
        lines.append(line)
        line = input("")
    testProg = "\n".join(lines)

    # If program halts on itself as input, go into an infinite loop
    if terminates(testProg, testProg):
        while True:
            pass    # a pass statement does nothing

main()

