# File  :   Ranking_algorithm.py
# Desc  :   This program demonstrate how to rank a simple inputted codes

import pandas as pd

df = pd.DataFrame({'Athlete': ['A','B','C'],
                   'Speed': [10,12,6],
                   'Endurance': [60,59,64]})

#I think you want 40% speed and 60% endurance right?
df['sorting_column'] = df.Speed*0.4 + df.Endurance*0.6
df.sort(columns='sorting_column')