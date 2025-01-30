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


freestyle50Men_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']

freestyle50Men_df.drop(columns = ['Unnamed: 0'], inplace = True)
freestyle50Men_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
freestyle50Men_df.drop(columns = ['Location'], inplace = True)
women50Remove = freestyle50Men_df[freestyle50Men_df['Gender'] == 'Women' ].index
freestyle50Men_df.drop(women50Remove, inplace = True)
free100DropMen = freestyle50Men_df[freestyle50Men_df['Distance (in meters)'] == '100m'].index
freestyle50Men_df.drop(free100DropMen, inplace = True)

freestyle50Men_df.to_csv('Freestyle_Men_50.csv')

freestyle50Women_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']

freestyle50Women_df.drop(columns = ['Unnamed: 0'], inplace = True)
freestyle50Women_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
freestyle50Women_df.drop(columns = ['Location'], inplace = True)
men50Remove = freestyle50Women_df[freestyle50Women_df['Gender'] == 'Men' ].index
freestyle50Women_df.drop(men50Remove, inplace = True)
free100DropWomen = freestyle50Women_df[freestyle50Women_df['Distance (in meters)'] == '100m'].index
freestyle50Women_df.drop(free100DropWomen, inplace = True)

freestyle50Women_df.to_csv('Freestyle_Women_50.csv')

# Combine the two dataframes for plotting
freestyle50Men_df['Gender'] = 'Men'
freestyle50Women_df['Gender'] = 'Women'
combined50_df = pd.concat([freestyle50Men_df, freestyle50Women_df])

# Create a line plot to compare Men's and Women's Freestyle Results over the years
fig = px.scatter(combined50_df, x='Year', y='Results', color='Gender', title="Men's vs Women's 50m Freestyle Results Over Time", labels={'Results': 'Result', 'Year': 'Year'}, hover_data=['Gender'])
fig.write_html('Men_v_Women_Freestyle_50m.html')