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

print(aggregated_df)
