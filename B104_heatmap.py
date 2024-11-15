#Programer : Johnson, Shawn 
#Programer : Chapdelaine, Adam 
#Course: ISAT B104
#Assignment: B104 Team 1
#File Name: B104_Data_Sheet_v2.csv

# importing modules needed
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# path = 'Project_Functions_1.py'
# dirname = os.path.dirname(__file__)

# #https://www.youtube.com/watch?v=0U9cs2V-Mqc&t=117s

# #Load the Excel file (only specific colums from an excel file)
# df = pd.read_excel('B104_Project.xlsx',
# sheet_name = 'B104_Project', 
# usecols = ['qn84', 'qn85', 'q2'])

# #group questions 'q2' - 'q84' - 'q85'
# sex_data = df.groupby('q2').size()
# print(sex_data)

# mental_data = df.groupby('qn84').size()
# print(mental_data)

# sleep_data = df.groupby('qn85').size()
# print(sleep_data)

# #Prints DataFram
# print(df)

# #heatmap_data = df 

# #creats a pivot table 
# heatmap_data = df.pivot_table(index='q2', columns='qn84', values='qn85', aggfunc=np.mean, fill_value=0)
# heatmap_data = df.pivot_table(index='q2', columns='qn85', values='qn84', aggfunc=np.mean, fill_value=0)

# #call the module seaborn 
# sns.heatmap(heatmap_data, annot=True)
# sns.heatmap(heatmap_data.corr())
# plt.show

# #line Plot


# # Load the data from the Excel file
# # Load the data

# df = pd.read_excel('B104_Project.xlsx',sheet_name = 'B104_Project')

# # Define the categorical data sleep hrs / mental health
# x = df['qn84']
# y = df['qn85']

# # Plot the data using scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, marker='o', color='b')
# plt.title('Mental Health Sleep Study')
# plt.xlabel('Mental Health')
# plt.ylabel('Sleep hrs')
# plt.grid(True)
# plt.show()




