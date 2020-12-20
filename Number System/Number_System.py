""" Number System Conversion """

import time

# Prints 0 to 10 octal, hexadecimal, and ASCII
print("INTEGER\t\t\tOCT\t\t\tHEX\t\t\tASCII")

for i in range(-100, 100):
    i += 1
    print(i, "      ", bin(i), "      ", oct(i), "      ", hex(i))
    time.sleep(0.5)
