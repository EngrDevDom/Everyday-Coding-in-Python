'''
    Data Analysis using Python : Slicing

    We can select specific ranges of our data in both
    the row and column directions using either label
    or integer-based indexing.
'''

import pandas as pd     # Using Pandas

web_data = {"Day": [1, 2, 3, 4, 5, 6], "Visitors": [1000, 700, 6000, 1000, 400, 350],
            "Bounce": [20, 30, 40, 20, 35, 20]}

df = pd.DataFrame(web_data)

print(df.head(2))
#     Day  Visitors  Bounce
# 0     1      1000      20
# 1     2       700      30

print(df.tail(2))
#     Day  Visitors  Bounce
# 4     5       400      35
# 5     6       350      20

