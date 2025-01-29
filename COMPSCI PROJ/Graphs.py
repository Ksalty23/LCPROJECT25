import pandas as pd
import plotly.express as px 

graphs_df = pd.read_csv('Cleaned_Olympic_Swimming_Results.csv')

unique_types = graphs_df['Stroke'].unique()
print(unique_types)

freestyle100Men_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']
backstroke_df = graphs_df[graphs_df['Stroke'] == 'Backstroke']
breaststroke_df = graphs_df[graphs_df['Stroke'] == 'Breaststroke']
butterfly_df = graphs_df[graphs_df['Stroke'] == 'Butterfly']

freestyle100Men_df.drop(columns = ['Unnamed: 0'], inplace = True)
freestyle100Men_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
freestyle100Men_df.drop(columns = ['Location'], inplace = True)
womenRemove = freestyle100Men_df[freestyle100Men_df['Gender'] == 'Women' ].index
freestyle100Men_df.drop(womenRemove, inplace = True)
free50DropMen = freestyle100Men_df[freestyle100Men_df['Distance (in meters)'] == '50m'].index
freestyle100Men_df.drop(free50DropMen, inplace = True)

print(freestyle100Men_df)
freestyle100Men_df.to_csv('Freestyle_Men_100.csv')

freestyle100Women_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']

freestyle100Women_df.drop(columns = ['Unnamed: 0'], inplace = True)
freestyle100Women_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
freestyle100Women_df.drop(columns = ['Location'], inplace = True)
menRemove = freestyle100Women_df[freestyle100Women_df['Gender'] == 'Men' ].index
freestyle100Women_df.drop(menRemove, inplace = True)
free50DropWomen = freestyle100Women_df[freestyle100Women_df['Distance (in meters)'] == '50m'].index
freestyle100Women_df.drop(free50DropWomen, inplace = True)

print(freestyle100Women_df)
freestyle100Women_df.to_csv('Freestyle_Women_100.csv')

# Combine the two dataframes for plotting
freestyle100Men_df['Gender'] = 'Men'
freestyle100Women_df['Gender'] = 'Women'
combined_df = pd.concat([freestyle100Men_df, freestyle100Women_df])

# Create a line plot to compare Men's and Women's Freestyle Results over the years
fig = px.scatter(combined_df, x='Year', y='Results', color='Gender', title="Men's vs Women's 100m Freestyle Results Over Time", labels={'Results': 'Result', 'Year': 'Year'}, hover_data=['Gender'])

"""allStrokesMen_df = pd.concat([freestyle_df, backstroke_df, breaststroke_df, butterfly_df])
allStrokesMen_df.drop(columns = ['Unnamed: 0'], inplace = True)
allStrokesMen_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
allStrokesMen_df.drop(columns = ['Location'], inplace = True)

womenRemove = allStrokesMen_df[ allStrokesMen_df['Gender'] == 'Women' ].index
allStrokesMen_df.drop(womenRemove, inplace = True)

print(allStrokesMen_df)


#This code will create a scatter plot of the 'Year' and 'Results' columns in my dataframe
fig = px.scatter(allStrokesMen_df, x='Year', y='Results, Distance (in meters), Team', title="Men's Olympic Swimming Results Over Time", labels={'Results': 'Result', 'Distance (in meters)': 'Distance'}, hover_data=['Distance (in meters)', 'Stroke'])"""

"""#This code will display the scatter plot in a new window
fig.write_html('Olympic_Swimming_Results.html')"""
fig.write_html('Mens_v_Womens_100m_Freestyle_Results.html')