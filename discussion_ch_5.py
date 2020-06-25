# File  :   discussion_ch_5.py
# Desc  :   Answers to Discussions Chapter 5 : Strings

s1 = "spam"
s2 = "ni!"

print("Result (a): ", "The Knights who say, " + s2)
print("Result (b): ", 3*s1 + 2*s2)
print("Result (c): ", s1[1])
print("Result (d): ", s1[1:3])
print("Result (e): ", s1[2] + s2[:2])
print("Result (f): ", s1 + s2[-1])
print("Result (g): ", s1.upper())
print("Result (h): ", s2.upper().ljust(4)*3)
