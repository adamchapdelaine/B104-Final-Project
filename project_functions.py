import matplotlib.pyplot as plt
import pandas as pd

# Opening and reading CSV data file

inputFile = open('B104_Data_Sheet_v2.csv')
df = pd.read_csv('B104_Data_Sheet_v2.csv')

# Renaming dataframe columns to their corresponding questions

df.rename(columns= {'q1':'Age', 'q2':'Sex', 'q3':'Grade', 'q4':'Hispanic', 'q5':'Race', 'q6':'Height', 'q7':'Weight', 'q84':'badMentalHealth', 'q85': 'hoursOfSleep'}, inplace=True) 

# Replacing int values for the dataframe column "Sex" with strings meant to convey meaning

df['Sex'].replace([1.0, 2.0], ['Female','Male'], inplace = True)

# Replacing int values for the dataframe column "badMentalHealth" with strings meant to convey meaning

df['badMentalHealth'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)

# Replacing int values for the dataframe column "hoursOfSleep" with strings meant to convey meaning

df['hoursOfSleep'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['4 hrs or less', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '10 hrs or more'], inplace = True)

# Get rid of word "count" on plot. 
# Pie charts merge over each other, don't display separately. Idk why

def getSleepPie():
    df['hoursOfSleep'] = df['hoursOfSleep'].replace(['4 hrs or less', '5 hrs', '6 hrs', '7 hrs', '9 hrs', '10 hrs or more'],"Not 8 hrs")
    df['hoursOfSleep'].value_counts(dropna=False).plot(kind="pie")

def getMentalHealthPie():
    df['badMentalHealth'] = df['badMentalHealth'].replace(['Never'],"Does not experience bad mental health")
    df['badMentalHealth'] = df['badMentalHealth'].replace(['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'],"Experiences bad mental health")
    plt.pie(df['badMentalHealth'])
    plt.show()
    # df['badMentalHealth'].value_counts(dropna=False).plot(kind="pie")

getSleepPie()
getMentalHealthPie()


print(df)

# # def getCorrel(file, var1, var2): # produces the correlation between data in two or more columns
# #     df = pd.read_csv(file)
# #     df = df.reset_index()
# #     output = (df[f'{var1}'].corr(df[f'{var2}'])) # will now take any variable fed into the function
# #     # print(df['q84'].corr(df['q85'])) # this line was just for debugging
# #     return output

# questionCorrel = getCorrel(fileData, 'q84', 'q85')

# print(questionCorrel) # negative correlation is greater now, sweet!
   

# def getHeatMap(file):
    
    
    







# # *below is a bunch of junk code*

# # filedata = pd.read_csv(fileData)
# # print(filedata.corr()) # correlation function with pandas, currently bugged.

# # def readFile(file):
# #     with open(file, mode= 'r') as file: # adding "as file" resolved issue with accessing internal file data 
# #         reader = csv.reader(file)
# #         for row in reader:
# #             print(row[0])

# # def getDataframe(dataFile): # creates a comprehensive dataframe of the contents of "B104_Data_Sheet.csv"
# #     with open(file, mode= 'r') as file:
# #         df = pd.read_csv(file)
# #     return df
    
# # df = getDataframe(fileData)

# # def isolateColumns(file): # Attempting to isolate columns from the dataframe, using pandas
# #     df = pd.read_csv(file)
# #     s = df[['q1','q2']] # Each successive column requires an additional set of brackets to avoid a KeyError
# #     return s

# # s = isolateColumns(fileData)

# # readFile(data)

# # print(df)

# # print(s)


# # failed for loop attempt

# # for index, row in df.iterrows():
# #     if row['q1'] != 5:
# #       df.drop(row, errors='ignore')
# #     df2 = pd.concat()

# # def sliceDataframe(file):
# #     df = pd.read_csv(file)
# #     df2 = pd.DataFrame()
    
# #     valueToRemove = 5
    
# #     df2 = df[df['q1'] != valueToRemove]
# #     print(df2['q1'])
    
# # sliceDataframe(fileData)   
