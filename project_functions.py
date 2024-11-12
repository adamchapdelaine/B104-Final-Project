import csv
import pandas as pd

data = ("B104_Data_Sheet.csv")

def readFile(file):
    with open(file, mode= 'r') as file: # adding "as file" resolved issue with accessing internal file data 
        reader = csv.reader(file)
        for row in reader:
            print(row[0])

def getColumns(file): # Attempting to create a dataframe with each column from the file, using pandas
    with open(file, mode= 'r') as file:
        reader = csv.reader(file)
        df = pd.DataFrame([reader], index = None) 
        for row in reader(df[1]):
            print(row)
            
getColumns(data)
  
    
# readFile(data)


# filedata = pd.read_csv(data)
# print(filedata.corr()) # correlation function with pandas, currently bugged.