import csv
import numpy as np
import pandas as pd

fileData = ("B104_Data_Sheet_v2.csv")

def getCorrel(file, var1, var2): # produces the correlation between data in two or more columns
    df = pd.read_csv(file)
    df = df.reset_index()
    output = (df[f'{var1}'].corr(df[f'{var2}'])) # will now take any variable fed into the function
    # print(df['q84'].corr(df['q85'])) # this line was just for debugging
    return output

questionCorrel = getCorrel(fileData, 'q84', 'q85')

print(questionCorrel) # negative correlation is greater now, sweet!
   

# *below is a bunch of junk code*

# filedata = pd.read_csv(fileData)
# print(filedata.corr()) # correlation function with pandas, currently bugged.

# def readFile(file):
#     with open(file, mode= 'r') as file: # adding "as file" resolved issue with accessing internal file data 
#         reader = csv.reader(file)
#         for row in reader:
#             print(row[0])

# def getDataframe(file): # creates a comprehensive dataframe of the contents of "B104_Data_Sheet.csv"
#     with open(file, mode= 'r') as file:
#         df = pd.read_csv(file)
#     return df
    
# df = getDataframe(fileData)

# def isolateColumns(file): # Attempting to isolate columns from the dataframe, using pandas
#     df = pd.read_csv(file)
#     s = df[['q1','q2']] # Each successive column requires an additional set of brackets to avoid a KeyError
#     return s

# s = isolateColumns(fileData)

# readFile(data)

# print(df)

# print(s)


# failed for loop attempt

# for index, row in df.iterrows():
#     if row['q1'] != 5:
#       df.drop(row, errors='ignore')
#     df2 = pd.concat()

# def sliceDataframe(file):
#     df = pd.read_csv(file)
#     df2 = pd.DataFrame()
    
#     valueToRemove = 5
    
#     df2 = df[df['q1'] != valueToRemove]
#     print(df2['q1'])
    
# sliceDataframe(fileData)   
