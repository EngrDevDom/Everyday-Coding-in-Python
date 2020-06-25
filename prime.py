# File  :   prime.py

def prime():
    a = b = 1
    for i in range(50):
        a += i
        b += i
        if a%b == 0:
            print(i)

prime()
