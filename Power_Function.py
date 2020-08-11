
''' Power Func #1 '''
def powr1(b, exp):
    myPowr = 1
    while exp > 0:
        myPowr *= ((~exp)&1) or b
        b *= b
        exp >>= 1       # Shift one bit right
    return myPowr

''' Power Func #2 '''
def powr2(b, exp):
    myPowr = 1
    while exp > 0:
        if exp%2 == 1:      # An odd exp means right-most bit is 1.
            myPowr *= b
        b *= b
        exp //= 2
    return myPowr

''' Power Func #3 '''
def pwr3(b, exp):
    return (not exp) or ((powr3(b, exp >> 1)**2) * (((~exp)&1) or b))

