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

df.rename(columns= {'q1':'Age', 'q2':'Sex', 'q3':'Grade', 'q4':'Hispanic', 'q5':'Race', 'q6':'Height', 'q7':'Weight', 'q84':'Poor MH', 'q85': 'Sleep Dur.'}, inplace=True) 

#-------------- Stage 3 --------------

#Generates a pie chart with data taken from CSV file.
def getPieCharts(): 
    # setting up data
    
    # 1st pie chart data
    dfAltered = df.copy()
    dfAltered['Sleep Dur.'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace = True)
    df2 = dfAltered['Sleep Dur.']
    df2 = df2.replace(['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs'],"Less than 8 hrs")
    df2 = df2.replace(['9 hrs', '≥ 10 hrs'],"More than 8 hrs")
    
    # 2nd pie chart data
    dfAltered['Poor MH'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    df3 = dfAltered['Poor MH']
    df3 = df3.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    df3 = df3.replace(['Never', 'Rarely'],'Rarely or never experiences bad mental health')
    
    
    # Establishing figure 
    fig, axs = plt.subplots(1, 2, figsize=(12, 9)) 
       
    # Creating Pie Chart 1
    
    valueCounts1 = df2.value_counts()
    axs[0].pie(valueCounts1, colors = sns.color_palette("crest"), autopct='%1.1f%%', explode=None)
    axs[0].set_title('Sleep Duration: Less, Equal, or More than 8 Hours')
    labels1 = ['Less than 8 hrs', '8 hrs', 'More than 8 hrs']
    axs[0].legend(labels = labels1, loc="upper right")
       
    # Creating Pie Chart 2
    
    valueCounts2 = df3.value_counts()
    axs[1].pie(valueCounts2, colors = sns.color_palette("crest"), autopct='%1.1f%%', explode=None)
    axs[1].set_title('Frequency of Bad Mental Health: Common vs. Rare')
    labels2 = ['Sometimes or Greater', 'Rarely or Never']
    axs[1].legend(labels = labels2, loc="upper right")

    # Show the plots
    plt.show()
    
def getBarChart1():  
    # 1st bar chart data
    dfAltered = df.copy()
    dfAltered['Poor MH'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace=True)
    dfAltered['Sex'].replace([1.0, 2.0], ['Female', 'Male'], inplace=True)
    df4 = dfAltered[['Poor MH', 'Sex']]
    df4 = df4.replace(['Sometimes', 'Mostly', 'Always'], 'Experiences bad mental health')
        # Establish balanced sample
    minCount = df4['Sex'].value_counts().min()
    balancedSample = df4.groupby('Sex').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
        # Filter for bad mental health experiences after balancing
    filteredDf = balancedSample[balancedSample['Poor MH'] == 'Experiences bad mental health']
        # Grouping "Bad Mental Health" to "Grade" for plotting student responses from each grade level
    groupedData = filteredDf['Sex'].value_counts().reset_index(name='count').rename(columns={'index': 'Sex'})
    
    # 2nd bar chart data
    dfAltered['Sleep Dur.'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace=True)
    df5 = dfAltered[['Poor MH', 'Sex', 'Sleep Dur.']]
    df5 = df5.replace(['Sometimes', 'Mostly', 'Always'], 'Experiences bad mental health')
        # Grouping for the second bar chart by Sleep Duration and Sex
    sleepGroupedData = dfAltered.groupby(['Sleep Dur.', 'Sex']).size().reset_index(name='count')
    
    # Establishing figure
    fig, axs = plt.subplots(1, 2, figsize=(12, 9))
      
    # Plotting the first bar chart
    sns.barplot(x='Sex', y='count', data=groupedData, ax=axs[0], palette="crest")
    axs[0].set_title('Reports of Bad Mental Health by Sex')
    axs[0].set_xlabel('Sex')
    axs[0].set_ylabel('Count of Students')
    
    # Plotting the second bar chart
    sns.barplot(x='Sleep Dur.', y='count', hue='Sex', data=sleepGroupedData, ax=axs[1], palette="crest")
    axs[1].set_title('Sleep Duration by Sex')
    axs[1].set_xlabel('Sleep Duration')
    axs[1].set_ylabel('Count of Students')
    
    # Show the plots
    plt.tight_layout()
    plt.show()
    
def getBarChart2():
    dfAltered = df.copy()
    dfAltered['Poor MH'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    dfAltered['Sleep Dur.'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace = True)
    df4 = dfAltered[['Poor MH', 'Sleep Dur.']]
    
    df4 = df4.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    
    # Drop value 'Other' from grades
    # df4 = df4.drop(df4[df4['Grade'] == 'Other'].index)
    
    # Calculate minimum count for balancing before filtering
    minCount = df4['Sleep Dur.'].value_counts().min()
    
    # Create proportional sample
    balancedSample = df4.groupby('Sleep Dur.').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
    
    # Filter for bad mental health experiences after balancing
    filteredDf = balancedSample[balancedSample['Poor MH'] == 'Experiences bad mental health']
    
    # Grouping "Bad Mental Health" to "Grade" for plotting student responses from each grade level
    groupedData = filteredDf['Sleep Dur.'].value_counts().reset_index(name='count').rename(columns={'index': 'Sleep Dur.'})
    
    # Plotting the data
    sns.barplot(x='Sleep Dur.', y='count', data=groupedData, order=['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], palette="crest")
    plt.xlabel('Hours of Sleep')
    plt.ylabel('Count of Students')
    plt.title('Reports of Bad Mental Health by Hours of Sleep')
    plt.show()
    
    # # Print counts
    # grouped_counts = filteredDf['Sleep Dur.'].value_counts()
    # print(grouped_counts)
    # print(minCount)
    
def getHeatMap():
    df.rename(columns= {'q84':'Poor MH', 'q85': 'Sleep Dur.'}, inplace=True) 
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
        
        try:
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
        
        except ValueError:
            print('Invalid value, please enter an integer.')
            continue
            
    print('\nThank you for viewing this project.')    
        

#This is the start of our drop down menu 
#-------------------------------------
display() 
