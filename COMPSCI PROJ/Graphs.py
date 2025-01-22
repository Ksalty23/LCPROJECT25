import pandas as pd
import plotly.express as px 

graphs_df = pd.read_csv('Cleaned_Olympic_Swimming_Results.csv')

unique_types = graphs_df['Stroke'].unique()
print(unique_types)

freestyle_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']
backstroke_df = graphs_df[graphs_df['Stroke'] == 'Backstroke']
breaststroke_df = graphs_df[graphs_df['Stroke'] == 'Breaststroke']
butterfly_df = graphs_df[graphs_df['Stroke'] == 'Butterfly']

freestyle_df.drop(columns = 'Unnamed: 0.1', inplace = True)
freestyle_df.drop(columns = 'Unnamed: 0', inplace = True)
freestyle_df.drop(columns = 'Location', inplace = True)

print(freestyle_df)
#This code will create a scatter plot of the 'Year' and 'Results' columns in my dataframe
fig = px.scatter(graphs_df, x = 'Year', y = 'Results', title = 'Olympic Swimming Results Over Time')

#This code will display the scatter plot in a new window
fig.write_html('Olympic_Swimming_Results.html')