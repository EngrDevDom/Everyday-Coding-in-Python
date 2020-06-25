"""
    File	      : Test_List_Stuff.py
    Description	  : This program uses the the Tester class
    Last Modified : 27.02.2020
    Author	      : Engr. Dom
"""

from tester import Tester

# sort has a bug (it has yet to be written)
def sort(lst):
    pass    # Sort not yet implemented

# sum has a bug (misses first element)
def sum(lst):
    total = 0
    for i in range(1, len(lst)):
        total += lst[i]
    return total

def main():
    t = Tester  # Make a test object
    # Some test cases to test sort
    col = [4, 2, 3]
    sort(col);
    t.check_equals("Sort test #1", [2, 3, 4], col)
    col = [2, 3, 4]
    sort(col);
    t.check_equals("Sort test #2", [2, 3, 4], col)
    # Some test cases to test sum
    t.check_equals("Sum test #1", sum([0, 3, 4]), 7)
    t.check_equals("Sum test #2", sum([-3, 0, 5]), 2)

    t.report_results()

main()  # Execute the program