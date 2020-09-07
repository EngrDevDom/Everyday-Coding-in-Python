''' Data Analysis using Python : Joining '''

import pandas as pd     # Using Pandas

# DataFrame 1
df1 = pd.DataFrame({"Index": [10, 30, 20, 40],
                    "GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

# DataFrame 2
df2 = pd.DataFrame({"Low_HPI": [1, 3, 2, 4],
                    "NNP": [40, 65, 85, 77]}, index=[2001, 2002, 2003, 2004])

join = df1.join(df2)        # This is the method

print(join)

# Output
#       Index  GDP  Low_HPI  NNP
# 2001     10   50        1   40
# 2002     30   45        3   65
# 2003     20   45        2   85
# 2004     40   67        4   77

