import random
import math
band = [1,2,3]
colors = ( "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white" )
band[0] = random.randint(0, 9)
band[1] = random.randint(0, 9)
band[2] = random.randint(0, 9)
for i in band:
    print(colors[i])
resist=(band[0]*10+band[1])*math.pow(10,band[2])
answ=int(input('now print the resistance\n'))
if resist == answ:
    print("nice")
    e=int(input('press enter to continue\n'))
else:
    print(f"nope, the resistance was {resist} ohms. Do you wanna to look at resistance table?\n y/n")
table=str(input())
if table == "y":
     print("fourth band is tolerance so we practically aren't using it\n           Band 1  Band 2  Band 3 (multipyer)\n    black    0       0       x1\n    brown    1       1       x10\n    red      2       2       x100\n    orange   3       3       x10^2\n    yellow   4       4       x10^3\n    green    5       5       x10^4\n    blue     6       6       x10^5\n    violet   7       7       x10^6\n    gray     8       8\n    white    9       9\n")
e=int(input('press enter to continue\n'))
