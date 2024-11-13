import csv
import numpy as np
import pandas as pd

data = ("B104_Data_Sheet.csv")

def getDataframe(file): # creates a comprehensive dataframe of the contents of "B104_Data_Sheet.csv"
    with open(file, mode= 'r') as file:
        df = pd.read_csv(file)
    return df
    
df = getDataframe(data)

def isolateColumns(file): # Attempting to isolate columns from the dataframe, using pandas
    df = pd.read_csv(file)
    s = df[['q1','q2']] # Each successive column requires an additional set of brackets to avoid a KeyError
    return s

s = isolateColumns(data)

def getCorrel(file): # produces the correlation between data in two or more columns
    df = pd.read_csv(file)
    print(df['qn84'].corr(df['qn85']))
            

print(df)

print(s)

getCorrel(data)
    
# readFile(data)


# filedata = pd.read_csv(data)
# print(filedata.corr()) # correlation function with pandas, currently bugged.

# def readFile(file):
#     with open(file, mode= 'r') as file: # adding "as file" resolved issue with accessing internal file data 
#         reader = csv.reader(file)
#         for row in reader:
#             print(row[0])