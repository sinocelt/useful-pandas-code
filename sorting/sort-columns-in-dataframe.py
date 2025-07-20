# © Justin Barry 2025-07
# watsontechworld.com
# you are free to use this code however you like. It would be nice if you give me credit but it isn't necessary. Enjoy!

import pandas as pd

df = pd.read_csv('salary.csv', delimiter='\t')

# show columns
# df.columns
# Out[3]: Index(['name', 'career', 'yearly_salary', 'gender', 'age', 'age_group'], dtype='object')

# sort by single columns

# sort data by 'name' column ascending
df.sort_values(by='name')

# example output should be something like

# name                        career  yearly_salary gender  age age_group
# 0     Brad                        doctor         150000      m   35     30–39
# 7   Cheryl   software engineering intern          68000      f   23     20–29
# 11    Jean                      waitress          30000      f   27     20–29
# 10    John         pizza delivery driver          30000      m   37     30–39
# 9    Julie                        author          80000      f   40     40–49
# 5     Leia             chemical engineer         112000      f   45     40–49
# 2     Luke                  data analyst          80000      m   39     30–39
# 14    Mary                        lawyer         300000      f   33     30–39
# 4     Mike                 account clerk          44630      m   25     20–29
# 6     Nick                           CEO         250000      m   57     50–59
# 15  Olivia                    day trader          80000      f   65     60–69
# 16   Pilar  entrepreneur / self-employed          55000      m   47     40–49
# 1     Sana                 idol / singer        1450000      f   28     20–29
# 13   Sarah                   Uber driver          40000      f   38     30–39
# 12   Sonja                     professor         150000      f   45     40–49
# 3     Tony                       teacher          45000      m   42     40–49
# 8    Wayne                        author          75000      m   75     70–79


# sort data by 'name' column descending
df.sort_values(by='name', ascending = False)

# output should be something like

#       name                        career  yearly_salary gender  age age_group
# 8    Wayne                        author          75000      m   75     70–79
# 3     Tony                       teacher          45000      m   42     40–49
# 12   Sonja                     professor         150000      f   45     40–49
# 13   Sarah                   Uber driver          40000      f   38     30–39
# 1     Sana                 idol / singer        1450000      f   28     20–29
# 16   Pilar  entrepreneur / self-employed          55000      m   47     40–49
# 15  Olivia                    day trader          80000      f   65     60–69
# 6     Nick                           CEO         250000      m   57     50–59
# 4     Mike                 account clerk          44630      m   25     20–29
# 14    Mary                        lawyer         300000      f   33     30–39
# 2     Luke                  data analyst          80000      m   39     30–39
# 5     Leia             chemical engineer         112000      f   45     40–49
# 9    Julie                        author          80000      f   40     40–49
# 10    John         pizza delivery driver          30000      m   37     30–39
# 11    Jean                      waitress          30000      f   27     20–29
# 7   Cheryl   software engineering intern          68000      f   23     20–29
# 0     Brad                        doctor         150000      m   35     30–39

# sort data by 'yearly_salary' column ascending
df.sort_values(by='yearly_salary', ascending = True)

#       name                        career  yearly_salary gender  age age_group
# 11    Jean                      waitress          30000      f   27     20–29
# 10    John         pizza delivery driver          30000      m   37     30–39
# 13   Sarah                   Uber driver          40000      f   38     30–39
# 4     Mike                 account clerk          44630      m   25     20–29
# 3     Tony                       teacher          45000      m   42     40–49
# 16   Pilar  entrepreneur / self-employed          55000      m   47     40–49
# 7   Cheryl   software engineering intern          68000      f   23     20–29
# 8    Wayne                        author          75000      m   75     70–79
# 15  Olivia                    day trader          80000      f   65     60–69
# 9    Julie                        author          80000      f   40     40–49
# 2     Luke                  data analyst          80000      m   39     30–39
# 5     Leia             chemical engineer         112000      f   45     40–49
# 12   Sonja                     professor         150000      f   45     40–49
# 0     Brad                        doctor         150000      m   35     30–39
# 6     Nick                           CEO         250000      m   57     50–59
# 14    Mary                        lawyer         300000      f   33     30–39
# 1     Sana                 idol / singer        1450000      f   28     20–29

# sort data by 'yearly_salary' column descending
df.sort_values(by='yearly_salary', ascending = False)

#      name                        career  yearly_salary gender  age age_group
# 1     Sana                 idol / singer        1450000      f   28     20–29
# 14    Mary                        lawyer         300000      f   33     30–39
# 6     Nick                           CEO         250000      m   57     50–59
# 0     Brad                        doctor         150000      m   35     30–39
# 12   Sonja                     professor         150000      f   45     40–49
# 5     Leia             chemical engineer         112000      f   45     40–49
# 9    Julie                        author          80000      f   40     40–49
# 2     Luke                  data analyst          80000      m   39     30–39
# 15  Olivia                    day trader          80000      f   65     60–69
# 8    Wayne                        author          75000      m   75     70–79
# 7   Cheryl   software engineering intern          68000      f   23     20–29
# 16   Pilar  entrepreneur / self-employed          55000      m   47     40–49
# 3     Tony                       teacher          45000      m   42     40–49
# 4     Mike                 account clerk          44630      m   25     20–29
# 13   Sarah                   Uber driver          40000      f   38     30–39
# 10    John         pizza delivery driver          30000      m   37     30–39
# 11    Jean                      waitress          30000      f   27     20–29


# NOTE it will actually do lexicographic sorting order

# to sort by career uncapitalized

# df.sort_values(by='career', key=lambda x: x.str.lower())
# Out[18]: 
#       name                        career  yearly_salary gender  age age_group
# 4     Mike                 account clerk          44630      m   25     20–29
# 8    Wayne                        author          75000      m   75     70–79
# 9    Julie                        author          80000      f   40     40–49
# 6     Nick                           CEO         250000      m   57     50–59
# 5     Leia             chemical engineer         112000      f   45     40–49
# 2     Luke                  data analyst          80000      m   39     30–39
# 15  Olivia                    day trader          80000      f   65     60–69
# 0     Brad                        doctor         150000      m   35     30–39
# 16   Pilar  entrepreneur / self-employed          55000      m   47     40–49
# 1     Sana                 idol / singer        1450000      f   28     20–29
# 14    Mary                        lawyer         300000      f   33     30–39
# 10    John         pizza delivery driver          30000      m   37     30–39
# 12   Sonja                     professor         150000      f   45     40–49
# 7   Cheryl   software engineering intern          68000      f   23     20–29
# 3     Tony                       teacher          45000      m   42     40–49
# 13   Sarah                   Uber driver          40000      f   38     30–39
# 11    Jean                      waitress          30000      f   27     20–29


# sort by 2 or more columns

# sort by career and then by name (note 2 people are authors so it will sort those twice). Do career ascending and name ascending too

# sort career so it is easier to sort later
df['career'] = df['career'].apply(lambda x: x.lower())


# use ascending option if I want ot manually choose ascending for each
df.sort_values(by=['career', 'name'], ascending = [True, True])
#       name                        career  yearly_salary gender  age age_group                      career_2
# 4     Mike                 account clerk          44630      m   25     20–29                 account clerk
# 9    Julie                        author          80000      f   40     40–49                        author
# 8    Wayne                        author          75000      m   75     70–79                        author
# 6     Nick                           ceo         250000      m   57     50–59                           ceo
# 5     Leia             chemical engineer         112000      f   45     40–49             chemical engineer
# 2     Luke                  data analyst          80000      m   39     30–39                  data analyst
# 15  Olivia                    day trader          80000      f   65     60–69                    day trader
# 0     Brad                        doctor         150000      m   35     30–39                        doctor
# 16   Pilar  entrepreneur / self-employed          55000      m   47     40–49  entrepreneur / self-employed
# 1     Sana                 idol / singer        1450000      f   28     20–29                 idol / singer
# 14    Mary                        lawyer         300000      f   33     30–39                        lawyer
# 10    John         pizza delivery driver          30000      m   37     30–39         pizza delivery driver
# 12   Sonja                     professor         150000      f   45     40–49                     professor
# 7   Cheryl   software engineering intern          68000      f   23     20–29   software engineering intern
# 3     Tony                       teacher          45000      m   42     40–49                       teacher
# 13   Sarah                   uber driver          40000      f   38     30–39                   uber driver
# 11    Jean                      waitress          30000      f   27     20–29                      waitress

# read more at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
