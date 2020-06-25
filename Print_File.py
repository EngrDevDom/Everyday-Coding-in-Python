# File  :   Print_File.py
# Desc  :   Prints a file to the screen.

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

main()
