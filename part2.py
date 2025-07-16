import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head(3))
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df[['Country name', 'Regional indicator']].head())
print(df[df['Healthy life expectancy']>0.7])