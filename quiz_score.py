# File  :   quiz_score.py
# Desc  :   A program that accepts an exam score and
#           prints out the corresponding grade.
# 5 = A, 4 = B, 3 = C, 2 = D, 0 & 1 = F

def main():
    score = int(input("Enter your score: "))
    grade = ["F", "F", "D", "C", "B", "A"]

    print("Your grade is:", grade[score])

main()
