"""
    Decomposing_Numbers.py
    Decomposing is when we break the number apart.
"""

while True:
    user = input('Enter a number: ')
    y = user[0] + "0" * (len(user)-1)
    res = ""
    z = int(user)
    for i in range(len(user)):
        if y == "0":    break
        else:
            res += y + " + "
            x = str(abs(int(y) - int(z)))
            z = int(x)
            y = (x[0] + "0" * (len(x)-1))
    print('Output :', res[0:-2])

