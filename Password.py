# Generate a password with length "passlen" with no duplicate characters

import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen = 8
p = "".join(random.sample(s,passlen))
print(p)