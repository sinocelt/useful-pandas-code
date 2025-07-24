import pandas as pd
import numpy as np

# to suppress some annoying messages
import warnings

# Suppress FutureWarnings
# I don't want annoying messages about agg
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('salary.csv', delimiter='\t')

# group by gender and get mean and median of salary
aggregated_df = df.groupby('gender')['yearly_salary'].agg([np.mean, np.median])


# grouped by gender
gender_group = df.groupby('gender')

print(aggregated_df)

# .first() show first in each group
# .last() show last in each group


# get first values for each column from grouped by gender
gender_group = df.groupby('gender')
first = gender_group.first()

print(first)
