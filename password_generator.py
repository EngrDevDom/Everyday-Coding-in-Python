# password_generator.py

import random

s = "abcdefghijkl\
    mnopqrstuvwxyz1234\
    567890ABCDEFGHIJKLM\
    NOPQRSTUVWXYZ!@#$%^&*\
    ()_-+[]{};/';.,"

password_len = 16
password = "".join(random.sample(s,password_len))
print(password)


