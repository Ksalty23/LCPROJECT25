import pandas as pd

#Loads the CSV file into a pandas DataFrame.
swim_df = pd.read_csv('Filtered_Swimming_Results.csv')

#This is a function to count colons in a string in the dataframe.
def count_colons(value):
    """This counts the number of colons (':') in the given value.
    - Converts the value to a string if it's not null (to handle non-string or NaN values).
    - Returns the colon count for the string."""
    value = str(value) if pd.notnull(value) else ''  #Converts non-null values to strings and also replaces NaN with an empty string (This prevents an error from occuring if the test comes across any Null values).
    return value.count(':')  #Use the string method count() to count colons.

#Apply the count_colons function to the 'Results' column.
#Creates a new column 'ColonCount' in the DataFrame.
swim_df['ColonCount'] = swim_df['Results'].apply(count_colons)

#Function to classify results based on the number of colons.
def classify_status(colon_count):
    """This then classifies the status as 'Passed' or 'Failed' based on the colon count.
    - 'Failed' if colon_count > 1.
    - 'Passed' otherwise."""
    return 'Failed' if colon_count > 1 else 'Passed'

#Applies the classify_status function to the 'ColonCount' column.
#Creates a new column 'Status' in the DataFrame.
swim_df['Status'] = swim_df['ColonCount'].apply(classify_status)

#Prints a summary of the results.
#Value counts for the 'Status' column provide the number of 'Passed' and 'Failed' rows.
print(swim_df['Status'].value_counts())


