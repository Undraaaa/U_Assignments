# Introduction-Python training
# Lecture 3: Data Types: Numpy and Pandas
# Assignment: Task1
# Created by Undral, Aug, 2022

''' Task-1 '''
import os
os.getcwd() # get current working directory
os.chdir(r"Aug27_lec3")

import pandas as pd
import numpy as np

'''
Q1. Add rows with arbitrary values to "data.xlsx" so that you have 50 rows in total 
'''
df_data = pd.read_excel("3_Data_table/data/data.xlsx")
df_data1= pd.read_excel("3_Data_table/data/data.xlsx")
df_data2= pd.read_excel("3_Data_table/data/data.xlsx")
df_data3= pd.read_excel("3_Data_table/data/data.xlsx")
df_data4= pd.read_excel("3_Data_table/data/data.xlsx")
type(df_data1)

df_data = df_data.append(df_data1, ignore_index = True)
df_data = df_data.append(df_data2, ignore_index = True)
df_data = df_data.append(df_data3, ignore_index = True)
df_data = df_data.append(df_data4, ignore_index = True)
print(df_data)
df_expand=df_data
df_expand.to_excel("3_Data_table/data/data50.xlsx") 
    '''
    for i in range(1,4):
        df_data = df_data.append(df_data{i}, ignore_index = True)
    '''

'''
Q2. Create a '.csv' file with data of only women older than 25 years old
'''
#df_data = pd.read_excel("3_Data_table/data/data.xlsx")
df_data.info()
df_data.head()
df_w25=df_data[(df_data["age"]>25) & (df["gender"] == "F")]
df_w25.to_csv("../U_Assignments/Section3/Women_25+.csv") 

'''
Q3. Create a '.json' file with data men under 23 years old
'''
#df_data = pd.read_excel("3_Data_table/data/data.xlsx")
df_data.info()
df_data.head()
df_w25=df_data[(df_data["age"]<23) & (df["gender"] == "M")]
df_w25.to_json("../U_Assignments/Section3/Man_23-.json") 


