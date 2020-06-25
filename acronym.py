# File  :   acronym.py
# Desc  :   A program that allows the user to type in a phrase and then
#           outputs the acronym for that phrase.

import re

words = input("Enter a phrase: ")

print(re.sub(r"([a-zA-Z])[a-z,A-Z]+\s*",r"\1", words).upper())
