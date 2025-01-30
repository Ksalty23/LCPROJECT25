#In this code, I will clean up my dataset using the 'pandas' package available in Thonny
import pandas as pd #This imports Pandas as a shorthand of 'pd'

swim_df = pd.read_csv('Filtered_Swimming_Results.csv') #This reads the entire CSV file into a Pandas dataframe

print('Shape BEFORE Cleaning (rows, cols): ', swim_df.shape) #This displays the number of rows/columns in my dataframe (PRE-CLEANING)

#Next, I'm going to remove any rows in my dataframe that contains a Null Value. For example: a blank space in one of the columns within that row
swim_df = swim_df.dropna()

#Now I remove any columns I won't need, such as the 'Relay?' column which adds nothing to my analysis of the dataset.
swim_df.drop(columns = 'Relay?', inplace = True)

#Now, I noticed that there are a few athletes who have a "DNS", "DNF" or "DQ" Value for their result. This means they did not complete the race or were disqualified! I'm going to remove any row that doesn't have a finishing time as their result.
index_DNF = swim_df[ swim_df['Results'] == 'Did not finish' ].index #This finds any rows that has a value of 'Did not finish' in the 'Results' column.
index_DNS = swim_df[ swim_df['Results'] == 'Did not start' ].index #This finds any rows that has a value of 'Did not start' in the 'Results' column.
index_DQ = swim_df[ swim_df['Results'] == 'Disqualified' ].index #This finds any rows that has a value of 'Disqualified' in the 'Results' column.

#The following 3 lines of code then remove the selected rows from the dataframe.
swim_df.drop(index_DNF, inplace = True) 
swim_df.drop(index_DNS, inplace = True)
swim_df.drop(index_DQ, inplace = True)


#Now I will print the length of the dataframe AFTER cleaning, to ensure these rows and columns were removed.
print('Shape AFTER Cleaning (rows, cols): ', swim_df.shape)

#This line ensures the 'Results' column is of string type for processing
swim_df['Results'] = swim_df['Results'].astype(str)

#Here I remove any rows where the value in 'Results' is not a valid numeric string
valid_results = swim_df['Results'].str.replace('.', '', 1).str.isdigit()
swim_df = swim_df[valid_results]

#This converts values in 'Results' to floats only
swim_df['Results'] = swim_df['Results'].astype(float)

print('Shape AFTER Removing Non-Numeric Results (rows, cols):', swim_df.shape)

#Now I will update my CSV file with the newly made changes to my dataframe.
swim_df.to_csv('Cleaned_Olympic_Swimming_Results.csv')