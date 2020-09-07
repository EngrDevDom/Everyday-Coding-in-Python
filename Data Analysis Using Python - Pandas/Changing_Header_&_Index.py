''' Data Analysis using Python : Changing Header & Index '''

import pandas as pd     # Using Pandas

# DataFrame
df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visits": [200, 300, 400, 500]})

df.set_index("Day", inplace=True)                       # Change Index

df = df.rename(columns = {"Visits": "Visitors"})        # Change Header

print(df)

# Output
#       Visitors
# Day
# 1         200
# 2         300
# 3         400
# 4         500

