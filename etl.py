import pandas as pd

data = pd.read_csv('source_data.csv')

data['date'] = pd.to_datetime(data['date'])
cleaned_data = data.dropna()

cleaned_data.to_csv('cleaned_data.csv')
