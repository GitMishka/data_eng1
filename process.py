import pandas as pd

df = pd.read_csv('data.csv')

mean_value = df['column_name'].mean()
print(f"Mean Value: {mean_value}")
