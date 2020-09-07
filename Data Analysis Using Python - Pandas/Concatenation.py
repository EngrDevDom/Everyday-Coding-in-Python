''' Data Analysis using Python : Concatenation '''

import pandas as pd     # Using Pandas

# DataFrame 1
df1 = pd.DataFrame({"Index": [10, 30, 20, 40],
                    "GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

# DataFrame 2
df2 = pd.DataFrame({"Index": [10, 30, 20, 40],
                    "GDP": [50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

concat = pd.concat([df1, df2])      # This is the method
print(concat)

# Output
#       Index  GDP
# 2001     10   50
# 2002     30   45
# 2003     20   45
# 2004     40   67
# 2005     10   50
# 2006     30   45
# 2007     20   45
# 2008     40   67

