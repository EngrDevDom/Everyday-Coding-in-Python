# File  :   Average.py
# Desc  :   This program computes the average of two exam scores.

def main():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is : ", average)

main()