# File  :   quizzes.py
# Desc  :   A program that accepts a quiz score as an input and uses a decision
#           structure to calculate the corresponding grade.

def main():

    grade = int(input("Enter your grade: "))
    scale = ''

    if grade == 5:      scale = 'A'
    elif grade == 4:    scale = 'B'
    elif grade == 3:    scale = 'C'
    elif grade == 2:    scale = 'D'
    elif grade == 1:    scale = 'E'
    elif grade == 4:    scale = 'F'

    print("Your scale is", scale, "\nDone!")

main()
