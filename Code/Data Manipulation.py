import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

heart_data = pd.read_csv('Heart Disease.csv')
# Checking if there are missing values
heart_data.isnull().sum()

print("---------- Analysis of ages ---------- ")
# The Average age of diagnosed with heart disease
average_age = heart_data[heart_data['target'] == 1]['age'].mean()
print("The average age of diagnosed with heart disease is {}.".format(round(average_age, 1)))

# The average between men and female age
male_vs_female_average_age = heart_data.groupby('sex').mean()['age']
print("The average age of a male is {} and female is {}.".format(round(male_vs_female_average_age[0], 2),
                                                                 round(male_vs_female_average_age[1], 2)))

# The max and min of ages
max_age = heart_data['age'].unique().max()
min_age = heart_data['age'].unique().min()
print("The oldest subject of this study is {} years old and the youngest is {} years old.".format(max_age, min_age))

# What is the difference between male and female who got diagnosed with heart disease?
plt.pie(heart_data.groupby('sex').sum()['target'], labels=["male", "female"], autopct='%1.1f%%')

# Is sex or chest pain indicates heart disease?
sex_and_chest_pain = heart_data.groupby(['cp', 'sex']).sum()['target']
unstacked_cp = sex_and_chest_pain.unstack(level=0)
unstacked_cp.plot(kind='bar')

# We noticed that a lot of subjects with heart disease got mild chest pain, Is high chest pain indicates heart disease?
age_chest_pain = heart_data.groupby(['cp', 'age']).sum()['target'].unstack(level=0).plot(kind='bar')

