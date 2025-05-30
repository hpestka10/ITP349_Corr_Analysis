# -*- coding: utf-8 -*-
"""Correlation_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VeFvv3mwRjzRGomtqls2p6YFWteHzN5S
"""

# PYTHON MODULES
# import user-installed modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pandas options
pd.set_option('display.max_rows', 100)

!wget -nc "https://raw.githubusercontent.com/hpestka10/ITP349_Corr_Analysis/refs/heads/main/happyscore_income.csv"

happiness_income_log = pd.read_csv('happyscore_income.csv')

# view columns and null counts for each column in the data frame
print(happiness_income_log.columns)
print(happiness_income_log.info())

# shape of the data frame
# happiness income log:
print("Happiness Income Log Shape:\n")
print(happiness_income_log.shape)

happiness_income_log.head()

# clean the happiness income log
df = happiness_income_log[['GDP', 'happyScore']]
print(df.head(),'\n')


print("Shape before dropping duplicates and unneeded columns: ")
print(df.shape,'\n')


df = df.drop_duplicates()
df = df.dropna()


print("Shape after dropping duplicates and unneeded columns: ")
print(df.shape)

df.head()

# To find the correlation among
# the columns using pearson method
df.corr(method ='pearson')

# To find the correlation among
# the columns using kendall method
df.corr(method='kendall')

# To find the correlation among
# the columns using spearman method
df.corr(method='spearman')

DF2 = happiness_income_log[['income_inequality', 'std_satisfaction']]

# To find the correlation among
# the columns using pearson method
DF2.corr(method ='pearson')