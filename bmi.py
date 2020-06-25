# File  :   bmi.py
# Desc  :   A program that calculates a person's BMI and prints a message
#           telling whether they are above, within, or below the healthy range.

def main():

    weight = float(input("Enter your weight(pounds): >> "))
    height = float(input("Enter your height(inches): >> "))
    status = ''

    bmi = (weight * 720) / (height ** 2)

    if bmi > 0 and bmi < 18:
        status = 'below'
    elif bmi >= 19 and bmi <=25:
        status = 'within'
    elif bmi >= 26:
        status = 'above'

    print("\nYou're bmi is", bmi)
    print("You are", status, "the healthy range.")

main()
