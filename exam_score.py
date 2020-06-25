# File  :   exam_score.py
# Desc  :   A program that accepts an exam score as input and
#           prints out the corresponding grade.
# 90-100 = A, 80-89 = B, 60-69 = D, <60 = F

def main():
    score = int(input("Enter your score: "))
    score.split()
    x = score[:1]
    grade = ["F", "F", "D", "C", "B", "A"]

    print("Your grade is:", grade[x])

main()
