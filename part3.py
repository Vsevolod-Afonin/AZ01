import pandas as pd

df = pd.read_csv('hh.csv')

df['Test'] = [new for new in range(29)]


# df.drop('Test', axis=1, inplace=True)
df.drop(28, axis=0, inplace=True)

print(df)