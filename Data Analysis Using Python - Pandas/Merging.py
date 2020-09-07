'''
    Data Analysis using Python : Merging

    Pandas provides a single function Merge, as
    the entry point for all standard database join
    operations between DataFrame Objects.
'''

import pandas as pd     # Using Pandas

# DataFrame 1
df1 = pd.DataFrame({"Index": [10, 30, 20, 40], "Tax_Rate": [2, 1, 2, 3],
                    "GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

# DataFrame 2
df2 = pd.DataFrame({"Index": [10, 30, 20, 40], "Tax_Rate": [2, 1, 2, 3],
                    "GDP": [50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

merge = pd.merge(df1, df2)      # This is the method
print(merge)

# Output
#       Index  Tax_Rate  GDP
# 0        10         2   50
# 1        30         1   45
# 2        20         2   45
# 3        40         3   67

