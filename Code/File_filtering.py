import pandas as pd

heart_data = pd.read_csv('Heart Disease.csv')
print(heart_data.isnull().sum())
# >>> No missing values found
heart_data.to_csv('Heart Disease_cleaned.csv')


