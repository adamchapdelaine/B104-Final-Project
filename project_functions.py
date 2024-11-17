import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#-------------- Stage 1 --------------
# Opening and reading CSV data file
inputFile = open('B104_Data_Sheet_v2.csv')
df = pd.read_csv('B104_Data_Sheet_v2.csv')

#-------------- Stage 2 --------------
# Changing the names of dataframe with corresponding colums

df.rename(columns= {'q1':'Age', 'q2':'Sex', 'q3':'Grade', 'q4':'Hispanic', 'q5':'Race', 'q6':'Height', 'q7':'Weight', 'q84':'badMentalHealth', 'q85': 'hoursOfSleep'}, inplace=True) 

#Changing the dataframe column "Sex" int values to strings that have significance
df['Sex'].replace([1.0, 2.0], ['Female', 'Male'], inplace = True)

# Changing
df['Grade'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['9th Grade', '10th Grade', '11th Grade', '12th Grade', 'Other'], inplace = True)


#Changing the dataframe column "badMentalHealth" int values to strings that have significance

df['badMentalHealth'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)

#Changing the dataframe column "hoursOfSleep" int values to strings that have significance

df['hoursOfSleep'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['4 hrs or less', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '10 hrs or more'], inplace = True)

#-------------- Stage 3 --------------
# Get rid of word "count" on plot. 
# Pie charts merge over each other, don't display separately. Idk why
#-------------------------------------
#Generates a pie chart with data taken from CSV file.
def getSleepPie():
    df2 = df['hoursOfSleep']
    df2 = df2.replace(['4 hrs or less', '5 hrs', '6 hrs', '7 hrs', '9 hrs', '10 hrs or more'],"Not 8 hrs")
    
    plt.figure(figsize=(8, 8))
    valueCounts1 = df2.value_counts()
    df2.value_counts().plot(kind='pie', subplots=True, figsize=(8, 8))
    valueCounts1.plot.pie(autopct='%1.1f%%')
    plt.title('Category 1 Distribution')
    plt.ylabel('')
    plt.show()

def getMentalHealthPie():
    df3 = df['badMentalHealth']
    df3 = df3.replace(['Never'],'Never experiences bad mental health')
    df3 = df3.replace(['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    
    plt.figure(figsize=(8, 8))
    valueCounts2 = df3.value_counts()
    df3.value_counts().plot(kind='pie', subplots=True, figsize=(8, 8))
    valueCounts2.plot.pie(autopct='%1.1f%%')
    plt.title('Category 2 Distribution')
    plt.ylabel('')
    plt.show()
    
def getBarChart():
    df4 = df[['badMentalHealth', 'Grade']]
    
    df4 = df4.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    
    # Drop value 'Other' from grades
    df4 = df4.drop(df4[df4['Grade'] == 'Other'].index)
    
    # Calculate minimum count for balancing before filtering
    minCount = df4['Grade'].value_counts().min()
    
    # Create proportional sample
    balancedSample = df4.groupby('Grade').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
    
    # Filter for bad mental health experiences after balancing
    filteredDf = balancedSample[balancedSample['badMentalHealth'] == 'Experiences bad mental health']
    
    # Grouping "badMentalHealth" to "Grade" for plotting student responses from each grade level
    groupedData = filteredDf['Grade'].value_counts().reset_index(name='count').rename(columns={'index': 'Grade'})
    
    # Plotting the data
    sns.barplot(x='Grade', y='count', data=groupedData, order=['9th Grade', '10th Grade', '11th Grade', '12th Grade'])
    plt.xlabel('Grade')
    plt.ylabel('Count of Students')
    plt.title('Bad Mental Health by Grade (Sometimes or Greater)')
    plt.show()
    
    # Print counts
    grouped_counts = filteredDf['Grade'].value_counts()
    print(grouped_counts)
    print(minCount)
    
    # df['badMentalHealth'].value_counts(dropna=False).plot(kind="pie"))

#-------------- Stage 4 --------------
#Prints input data of Stage 3 and displays needed charts 
getSleepPie()
getMentalHealthPie()
getBarChart()

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
