import pandas as pd

#Loads the CSV file.
swim_df = pd.read_csv('Olympic_Swimming_Results_1912to2020.csv')

#I'm going to re-use the function to count colons in a string from my Test file, and then I will drop any rows that contain more than 1 colon in the 'Results' column.
def count_colons(value):
    
    value = str(value) if pd.notnull(value) else ''  #Converts non-null values to string, replace NaN with an empty string.
    return value.count(':')  #Here I used the string method count() to count the number of colons.

#Here I'll apply the count_colons function to the 'Results' column.
swim_df['ColonCount'] = swim_df['Results'].apply(count_colons)

#This filters the DataFrame to keep only rows where ColonCount is less than or equal to 1.
filtered_df = swim_df[swim_df['ColonCount'] <= 1]

#I'm going to drop the 'ColonCount' column that was created as it's no longer needed in the dataframe.
filtered_df = filtered_df.drop(columns=['ColonCount'])

#Saves the filtered DataFrame to a new CSV file.
filtered_df.to_csv('Filtered_Swimming_Results.csv')

#Prints the first few rows of the filtered DataFrame for verification.
print(filtered_df.head())
