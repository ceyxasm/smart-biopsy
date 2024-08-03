import pandas as pd

df = pd.read_csv('../RT-CT-CPTAC-UCEC-correspondence.csv')
print( list( df['CT-Series-ID']))
