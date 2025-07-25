# © Justin Barry 2025-07
# watsontechworld.com
# you are free to use this code however you like. It would be nice if you give me credit but it isn't necessary. Enjoy!

import pandas as pd

# make a dataframe with a dictionary
# note the keys of the dictionary will be the columns
# they will map to the values and the values are the row values. The values must be in a list
# Furthermore, if you have multiple columns, each column's values list need to have the same number of values

data = {
    'name': ['robert', 'richard', 'maximus', 'olivia', 'mia', 'sydney', 'reina', 'takeshi', 'sakura'],
    'age': [33, 35, 34, 28, 22, 40, 21, 29, 25],
    'career': ['linguist', 'teacher', 'doctor', 'engineer', 'clerk', 'manager', 'driver', 'nurse', 'YouTuber'],
    'fav_hobby': ['reading', 'watching tv', 'fishing', 'rock climbing', 'bowling', 'playing video games', 'working out', 'painting', 'chess'],
}

# create dataframe from dictionary
df = pd.DataFrame(data=data)

print(df)






# import a csv into a dataframe
# use salary.csv which is a salary table
# optionally add the delimiter to make sure it is parsed correctly. In this case, I'll use tab as the delimiter.
salary_df = pd.read_csv('salary.csv', delimiter='\t')

print(salary_df)


# Series

# make a series from original df

name_series = df.name

print(name_series)

print(type(name_series))




name_series = df.name

print(name_series)

print(type(name_series))


USE JUPYPTER NOTEBOOK FILE?



####

POST ABOUT useful pandas code


with jupyter notebook








