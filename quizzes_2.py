# File  :   quizzes_2.py
# Desc  :   A program that accepts a quiz score as an input and uses a decision
#           structure to calculate the corresponding grade.

def main():

    grade = int(input("Enter your grade: "))
    scale = ''

    if grade <= 100 or grade >= 90:    scale = 'A'
    elif grade <= 89 or grade > 80:    scale = 'B'
    elif grade <= 79 or grade > 70:    scale = 'C'
    elif grade <= 69 or grade > 60:    scale = 'D'
    elif grade <= 60:                  scale = 'F'

    print("Your scale is", scale, "\nDone!")

main()
