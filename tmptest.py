import sys
import os
import pandas as pd

file = "/Users/malhal/Downloads/SRA_75K.csv"
data= pd.read_csv(file)

mb_size = data['size_MB'].sum()
gb_size = mb_size/1000

print (gb_size)
