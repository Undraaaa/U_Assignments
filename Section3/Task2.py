# Introduction-Python training
# Lecture 3: Data Types: Numpy and Pandas
# Assignment: Task1
# Created by Undral, Aug, 2022

''' Task-2 '''

import pandas as pd
import numpy as np

import os
os.getcwd() # get current working directory 
#os.chdir(r'Aug27_lec3/3_Data_table')


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df_data = pd.read_excel("./3_Data_table/data/data50.xlsx")
df_data.info()

'''
Q1. What are the values in row 17 and column 2-5 of dataframe created from "data.xlsx"
'''
df_data.head(18) 
filter1=df_data.iloc[17,2:6] 
filter1.values.tolist()

'''
Q2. What are the values row 25-28 and column 'firstName, age' of dataframe created from "data.xlsx"
'''
df_data.head(30) 
df_data.loc[25:28,("firstName", "age")]  

'''
Q3. Find the lowest, the highest and mean salary and age for men and women seprately using 'groupby'
'''
lowest=df_data.groupby("gender")['salary'].min() 
lowest.to_dict()
highest=df_data.groupby("gender")['salary'].max() 
highest.to_dict()
mean=df_data.groupby('gender')['salary'].mean() 
mean.to_dict()

'''
Q4. Find the lowest, the highest and mean salary and for men and women separately using 'pivot table'
'''

table_mean = pd.pivot_table(df_data, values=['salary'], index=['gender'], aggfunc=np.mean )
table_min = pd.pivot_table(df_data, values=['salary'], index=['gender'], aggfunc=np.min )
table_max = pd.pivot_table(df_data, values=['salary'], index=['gender'], aggfunc=np.max )
print(table_mean)
print(table_min)
print(table_max)

#table = pd.pivot_table(df_data, values=['salary'], index=['gender'], aggfunc={'salary': 'mean','salary': 'min','salary':'max'} )
#print(table)

