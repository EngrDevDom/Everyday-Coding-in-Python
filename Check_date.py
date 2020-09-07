# This program checks if the date format input is correct.

check = [
    [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]

day, month, year = map(int, input("Give a date: ").split())
feb_29 = int(year%400 == 0 or (year%4 == 0 and year%100 != 0))

if month < 13 and month > 0:
    if day > 0 and day <= check[feb_29][month]:
        print("CORRECT!")
    else:
        print("INCORRECT!")
else:
    print("INCORRECT!")

