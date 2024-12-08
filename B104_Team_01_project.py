## Developers:          Chapdelaine, Adam / Johnson, Shawn
## Course:              CSCI/ISAT - B104
## Project:             B104 Final Project
## Team Name:           Team Lunchbox
## Team Number:         01


# Core Imported Libraries
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Optional GUI Libraries
import ctypes
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    # Third-Party (Open Source) Tkinter Theme Package
import sv_ttk


# Ignore miscellaneous warnings during program execution
warnings.filterwarnings('ignore')


#-------------- Stage 1 --------------
# Opening and reading the .csv excel data file
inputFile = open('B104_Team_01_YRBS_data.csv')
df = pd.read_csv('B104_Team_01_YRBS_data.csv')


#-------------- Stage 2 --------------
# Renaming dataframe columns for human convenience 
df.rename(columns= {'q1':'Age', 'q2':'Sex', 'q3':'Grade', 'q4':'Hispanic', 'q5':'Race', 'q6':'Height', 'q7':'Weight', 'q84':'Poor MH', 'q85': 'Sleep Dur.'}, inplace=True) 


#-------------- Stage 3 --------------
# Generate data visualization charts

    # Generate dual pie charts
def getPieCharts(): 
        # Preparing data snippets for each pie chart
            # 1st pie chart snippet
    dfAltered = df.copy()
    dfAltered['Sleep Dur.'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace = True)
    dfSnippet = dfAltered['Sleep Dur.']
    dfSnippet = dfSnippet.replace(['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs'],'Less than 8 hrs')
    dfSnippet = dfSnippet.replace(['9 hrs', '≥ 10 hrs'],'More than 8 hrs')
    
            # 2nd pie chart snippet
    dfAltered['Poor MH'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    dfSnippet2 = dfAltered['Poor MH']
    # dfSnippet2 = dfSnippet2.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
    dfSnippet2 = dfSnippet2.replace(['Never', 'Rarely'],'Rarely or never experiences bad mental health')
    
    
        # Establishing chart figure containing two subplots 
    fig, axs = plt.subplots(1, 2, figsize=(12, 9)) 
          
    
        # Displaying each pie chart on figure
            # 1st pie chart display
    valueCounts1 = dfSnippet.value_counts()
    axs[0].pie(valueCounts1, colors = sns.color_palette('crest'), autopct='%1.1f%%', explode=None)
    axs[0].set_title('Sleep Duration: Less, Equal, or More than 8 Hours')
    labels1 = ['Less than 8 hrs', '8 hrs', 'More than 8 hrs']
    axs[0].legend(labels = labels1, loc='upper left')
       
            # 2nd pie chart display
    valueCounts2 = dfSnippet2.value_counts()
    axs[1].pie(valueCounts2, colors = sns.color_palette('crest'), autopct='%1.1f%%', explode=None)
    axs[1].set_title('Frequency of Bad Mental Health: Common vs. Rare')
    labels2 = ['Rarely & Never', 'Sometimes', 'Mostly', 'Always']
    axs[1].legend(labels = labels2, loc='upper left')


        # Display figure when function is called
    return fig


    # Generate single bar chart
def getBarChartSolo():
        # Preparing data snippets for bar chart
    dfAltered = df.copy()
    dfAltered['Poor MH'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace = True)
    dfAltered['Sleep Dur.'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace = True)
    dfSnippet = dfAltered[['Poor MH', 'Sleep Dur.']]
    dfSnippet = dfSnippet.replace(['Sometimes', 'Mostly', 'Always'],'Experiences bad mental health')
            # Establish proportional sample as males outnumber females in the original sample
    minCount = dfSnippet['Sleep Dur.'].value_counts().min()
    balancedSample = dfSnippet.groupby('Sleep Dur.').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
            # Filter data selection for bad mental health experiences
    filteredDf = balancedSample[balancedSample['Poor MH'] == 'Experiences bad mental health']
            # Count how many students reported bad mental health experiences for each category of sleep duration
    groupedData = filteredDf['Sleep Dur.'].value_counts().reset_index(name='count').rename(columns={'index': 'Sleep Dur.'})
    
        # Establishing chart figure containing one subplot
    fig, axs = plt.subplots(figsize=None)
    
        # Displaying the bar chart
    sns.barplot(x='Sleep Dur.', y='count', data=groupedData, order=['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], palette='crest')
    plt.xlabel('Hours of Sleep')
    plt.ylabel('Count of Students')
    plt.title('Reports of Bad Mental Health by Hours of Sleep')
    
    
        # Display figure when function is called
    return fig


    # Generate dual bar charts
def getBarChartDuo():  
        # Preparing data snippets for each pie chart
            # 1st bar chart snippet
    dfAltered = df.copy()
    dfAltered['Poor MH'].replace([1.0, 2.0, 3.0, 4.0, 5.0], ['Never', 'Rarely', 'Sometimes', 'Mostly', 'Always'], inplace=True)
    dfAltered['Sex'].replace([1.0, 2.0], ['Female', 'Male'], inplace=True)
    dfSnippet = dfAltered[['Poor MH', 'Sex']]
    dfSnippet = dfSnippet.replace(['Sometimes', 'Mostly', 'Always'], 'Experiences bad mental health')
                # Establish proportional sample as males outnumber females in the original sample
    minCount = dfSnippet['Sex'].value_counts().min()
    balancedSample = dfSnippet.groupby('Sex').apply(lambda x: x.sample(minCount, random_state=42)).reset_index(drop=True)
                # Filter data selection for bad mental health experiences
    filteredDf = balancedSample[balancedSample['Poor MH'] == 'Experiences bad mental health']
                # Count how many students in the filtered dataframe belong to each sex
    groupedData = filteredDf['Sex'].value_counts().reset_index(name='count').rename(columns={'index': 'Sex'})
    
            # 2nd bar chart snippet
    dfAltered['Sleep Dur.'].replace([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], ['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], inplace=True)
    dfSnippet2 = dfAltered[['Poor MH', 'Sex', 'Sleep Dur.']]
    dfSnippet2 = dfSnippet2.replace(['Sometimes', 'Mostly', 'Always'], 'Experiences bad mental health')
                # Grouping the data by sleep duration and sex
    sleepGroupedData = dfAltered.groupby(['Sleep Dur.', 'Sex']).size().reset_index(name='count')
    
    
        # Establishing chart figure containing two subplots 
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
      
    
        # Displaying each pie chart on figure
            # 1st bar chart display
    sns.barplot(x='Sex', y='count', data=groupedData, ax=axs[0], palette='crest')
    axs[0].set_title('Reports of Bad Mental Health by Sex')
    axs[0].set_xlabel('Sex')
    axs[0].set_ylabel('Count of Students')
    
            # 2nd pie chart display
    sns.barplot(x='Sleep Dur.', y='count', hue='Sex', data=sleepGroupedData, ax=axs[1], order=['≤ 4 hrs', '5 hrs', '6 hrs', '7 hrs', '8 hrs', '9 hrs', '≥ 10 hrs'], palette='crest')
    axs[1].set_title('Sleep Duration by Sex')
    axs[1].set_xlabel('Sleep Duration')
    axs[1].set_ylabel('Count of Students')
    
    
        # Display figure when function is called
    return fig
    
    
    # Generate heatmap
def getHeatmap():
        # Renaming data columns for heatmap display
    df.rename(columns= {'q84':'Poor MH', 'q85': 'Sleep Dur.'}, inplace=True) 
    
    fig, axs = plt.subplots(figsize=None)
    
    
        # Display heatmap
    sns.heatmap(df.corr(numeric_only=True),  cmap='crest', annot=True)
    
    plt.tight_layout()
        # Display figure when function is called
    return fig
    
    
#-------------- Stage 4 --------------
# Generate display
def display():
    print('\nChart Menu:')
    print('--------------------------------------------------') 
    print('Options:\n\nPie Charts \t\t(Sleep & Mental Health) \t= \t0\nSolo Bar Chart \t(Sleep & Mental Health) \t= \t1\nDual Bar Chart \t(Mental Health & Gender) \t= \t2\nComprehensive Heatmap \t\t\t\t\t\t= \t3')
    
    
    # While loop contains user interface
    while True:
        userCheck = 'Y'
        breaker = False
        
        # Implementing 'try' function to test for exception error
        try:
            userInput = int(input('\nSelect 0-3 from the visual data list:\t\t\t'))
            
            if userInput == 0:
                getPieCharts() 
                plt.show()
                
            elif userInput == 1:
                getBarChartSolo()
                plt.show()
            
            elif userInput == 2:
                getBarChartDuo()
                plt.show()
                
            elif userInput == 3:
                getHeatmap()
                plt.show()
                
            else:
                print('Invalid selection. Please select a number between 0 and 3.') 
                continue
        
            while True: 
                userCheck = input('\nWould you like to continue? (Y/N):\t\t\t\t').lower()
                if userCheck == ('y'):
                    break
                elif userCheck == ('n'):
                    breaker = True
                    break
                else:
                    print('Invalid selection, please enter: ("Y" or "N")')
            
            if breaker == True:
                break
            
        # Except function to handle exception error (user submitting str instead of int)
        except ValueError:
            print('Invalid value, please enter an integer.')
            continue
        
    
    print('\n\nThanks for viewing this project!')    


# Executing display function below 
#-------------------------------------
display() 


# #-------------- Stage 4.5 (Bonus) --------------
# # Generate UI display


#     # Pre-emptively increasing screen resolution 
# ctypes.windll.shcore.SetProcessDpiAwareness(1)


#     # Creating empty root window
# root = tk.Tk()
# root.title('B104 Project Graphs')


#     # Establishing mainframe window with a grid where all widgets will be placed
# mainframe = ttk.Frame(root, padding='12 3 12 12')
# mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)


#     # Creating title for root window
# label = tk.Label(mainframe, text='Chart Menu:')
# label.pack()
# label.pack(padx = 5, pady = 5)


#     # Creating blank canvas to refresh
# canvas = None


#     # Process user input & draw canvas selection 
# def getCanvasChoice(choice):  
#     if choice == 1:
#         fig = getPieCharts()
#     elif choice == 2:
#         fig = getBarChartSolo()
#     elif choice == 3:
#         fig = getBarChartDuo()
#     elif choice == 4:
#         fig = getHeatmap()
    
    
#         # Function to display canvas in application
#     def drawCanvas(fig):
#             # This avoids a "referenced before assignment" error
#         global canvas
#             # Clearing previous canvas so a new one can be displayed
#         if canvas is not None:
#             canvas.get_tk_widget().destroy()
#         canvas = FigureCanvasTkAgg(fig, master=mainframe)
#         canvas.draw()
#         canvas.get_tk_widget().pack(padx=15, pady=20)
        
#         # Running the function after all previous lines
#     drawCanvas(fig)

    
#     # Creating four buttons for users to select graph of their choosing
#         # Button #1
# chartButton1 = ttk.Button(mainframe, text='Pie Charts (Sleep & Mental Health)', command=lambda: getCanvasChoice(1))
# chartButton1.pack()
# chartButton1.pack(padx = 5, pady = 3)

#         # Button #2
# chartButton2 = ttk.Button(mainframe, text='Solo Bar Chart (Sleep & Mental Health)', command=lambda: getCanvasChoice(2))
# chartButton2.pack()
# chartButton2.pack(padx = 5, pady = 3)

#         # Button #3
# chartButton3 = ttk.Button(mainframe, text='Dual Bar Chart (Mental Health & Gender)', command=lambda: getCanvasChoice(3))
# chartButton3.pack()
# chartButton3.pack(padx = 5, pady = 3)
    
#         # Button # 4
# chartButton4 = ttk.Button(mainframe, text='Comprehensive Heatmap', command=lambda: getCanvasChoice(4))
# chartButton4.pack()
# chartButton4.pack(padx = 5, pady = 3)


#     # Adding a quit button placed on the bottom of the application window
# quitButton = ttk.Button(mainframe, text='Quit', command=root.destroy)
# quitButton.pack(side='bottom', padx=15, pady=20)


# # Set application to dark theme
# sv_ttk.set_theme("dark")


# # Making window visible
# root.mainloop()


# # Thank you message (For UI interface)
# print('\n\nThanks for viewing this project!')  
    