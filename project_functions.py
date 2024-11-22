import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

warnings.filterwarnings("ignore")

#-------------- Stage 1 --------------
# Opening and reading CSV data file
inputFile = open('B104_Data_Sheet_v2.csv')
df = pd.read_csv('B104_Data_Sheet_v2.csv')

#-------------- Stage 2 --------------
# Changing the names of dataframe with corresponding colums

df.rename(columns= {'q1':'Age', 'q2':'Sex', 'q3':'Grade', 'q4':'Hispanic', 'q5':'Race', 'q6':'Height', 'q7':'Weight', 'q84':'Bad Mental Health', 'q85': 'Sleep Duration'}, inplace=True) 

#-------------- Stage 3 --------------

#Generates a pie chart with data taken from CSV file.
def getPieCharts(): 
    # setting up data
    
    # 1st pie chart data
    dfAltered = df.copy()
    dfAltered['Sleep Duration'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace = True)
    df2 = dfAltered['Sleep Duration']
    df2 = df2.replace(['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs'],"Less than 8 hrs")
    df2 = df2.replace(['9 hrs', '≥ 10 hrs'],"More than 8 hrs")
    
    # 2nd pie chart data
    dfAltered['Bad Mental Health'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    df3 = dfAltered['Bad Mental Health']
    df3 = df3.replace(['Never', 'Rarely'],'Rarely or never experiences bad mental health')
    df3 = df3.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    
    # Establishing figure 
    fig, axs = plt.subplots(1, 2, figsize=(12, 9)) 
       
    # Creating Pie Chart 1
    
    valueCounts1 = df2.value_counts()
    axs[0].pie(valueCounts1, colors = sns.color_palette("crest"), autopct='%1.1f%%', explode=None)
    axs[0].set_title('Category 1 Distribution')
    labels1 = ['Less than 8 hrs', '8 hrs', 'More than 8 hrs']
    axs[0].legend(labels = labels1, loc="upper right")
       
    # Creating Pie Chart 2
    
    valueCounts2 = df3.value_counts()
    axs[1].pie(valueCounts2, colors = sns.color_palette("crest"), autopct='%1.1f%%', explode=None)
    axs[1].set_title('Experiences bad Mental Health (Sometimes or Greater)')
    labels2 = ['Rarely or Never', 'Sometimes or Greater']
    axs[1].legend(labels = labels2, loc="upper right")


    plt.show()
    
def getBarChart1():
    dfAltered = df.copy()
    dfAltered['Bad Mental Health'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    dfAltered['Sex'].replace([1.0, 2.0], ['Female', 'Male'], inplace = True)
    df4 = dfAltered[['Bad Mental Health', 'Sex']]
    
    df4 = df4.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    
    # Calculate minimum count for balancing before filtering
    minCount = df4['Sex'].value_counts().min()
    
    # Create proportional sample
    balancedSample = df4.groupby('Sex').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
    
    # Filter for bad mental health experiences after balancing
    filteredDf = balancedSample[balancedSample['Bad Mental Health'] == 'Experiences bad mental health']
    
    # Grouping "Bad Mental Health" to "Grade" for plotting student responses from each grade level
    groupedData = filteredDf['Sex'].value_counts().reset_index(name='count').rename(columns={'index': 'Sex'})
    
    # Plotting the data, custom color palette (color added with 'palette' line 127)
    sns.barplot(x='Sex', y='count', data=groupedData, order=['Female', 'Male'], palette="crest")
    plt.xlabel('Sex')
    plt.ylabel('Count of Students')
    plt.title('Bad Mental Health by Sex (Sometimes or Greater)')
    plt.show()
    
def getBarChart2():
    dfAltered = df.copy()
    dfAltered['Bad Mental Health'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    dfAltered['Sleep Duration'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace = True)
    df4 = dfAltered[['Bad Mental Health', 'Sleep Duration']]
    
    df4 = df4.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    
    # Drop value 'Other' from grades
    # df4 = df4.drop(df4[df4['Grade'] == 'Other'].index)
    
    # Calculate minimum count for balancing before filtering
    minCount = df4['Sleep Duration'].value_counts().min()
    
    # Create proportional sample
    balancedSample = df4.groupby('Sleep Duration').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
    
    # Filter for bad mental health experiences after balancing
    filteredDf = balancedSample[balancedSample['Bad Mental Health'] == 'Experiences bad mental health']
    
    # Grouping "Bad Mental Health" to "Grade" for plotting student responses from each grade level
    groupedData = filteredDf['Sleep Duration'].value_counts().reset_index(name='count').rename(columns={'index': 'Sleep Duration'})
    
    # Plotting the data
    sns.barplot(x='Sleep Duration', y='count', data=groupedData, order=['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], palette="crest")
    plt.xlabel('Hours of Sleep')
    plt.ylabel('Count of Students')
    plt.title('Bad Mental Health by Sleep (Sometimes or Greater)')
    plt.show()
    
    # # Print counts
    # grouped_counts = filteredDf['Sleep Duration'].value_counts()
    # print(grouped_counts)
    # print(minCount)
    
def getHeatMap():
    df.rename(columns= {'q84':'Bad Mental Health', 'q85': 'Sleep Duration'}, inplace=True) 
    sns.heatmap(df.corr(numeric_only=True),  cmap="crest", annot=True)
    plt.show()
    
    # Note: Sex displays as negative correlation, could be reversed to positive, both are valid. Revisit later.

def display():
    print('\nChart Menu:')
    print('--------------------------------------------------') 

    # Task 4 Determine if the number provided by the user is prime
    print('Options:\n\nPie Charts (Sleep & Mental Health) = 0\nBar Chart (Mental Health & Gender) = 1\nBar Chart (Sleep & Mental Health) = 2\nComprehensive Heatmap = 3')

    while True:
        userCheck = 'Y'
        userInput = int(input('\nSelect 0-3 from the visual data list:\t'))
        
        if userInput == 0:
            getPieCharts()
            
            userCheck = input('\nWould you like to continue? (Y/N):\t').lower()
            if userCheck == ('y'):
                continue
            else:
                break
            
            
        elif userInput == 1:
            getBarChart1()
            
            userCheck = input('Would you like to continue? (Y/N):\t').lower()
            if userCheck == 'y':
                continue
            else:
                break
        
        elif userInput == 2:
            getBarChart2()
            
            userCheck = input('Would you like to continue? (Y/N):\t').lower()
            if userCheck == 'y':
                continue
            else:
                break
            
        elif userInput == 3:
            getHeatMap()
            
            userCheck = input('Would you like to continue? (Y/N):\t').lower()
            if userCheck == 'y':
                continue
            else:
                break
            
        else:
            print('Invalid selection. Please select a number between 0 and 3.') 
    print('\nThank you for viewing this project.')

#This is the start of our drop down menu 
#-------------------------------------
display() 
