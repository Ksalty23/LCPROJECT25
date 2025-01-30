import plotly.express as px
import pandas as pd

graphs_df = pd.read_csv('Cleaned_Olympic_Swimming_Results.csv')

freestyle50Men_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']

freestyle50Men_df.drop(columns = ['Unnamed: 0'], inplace = True)
freestyle50Men_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
freestyle50Men_df.drop(columns = ['Location'], inplace = True)
firstplacemenonly = freestyle50Men_df[freestyle50Men_df['Rank'] != 1].index
freestyle50Men_df.drop(firstplacemenonly, inplace = True)
women50Remove = freestyle50Men_df[freestyle50Men_df['Gender'] == 'Women' ].index
freestyle50Men_df.drop(women50Remove, inplace = True)
free100DropMen = freestyle50Men_df[freestyle50Men_df['Distance (in meters)'] == '100m'].index
freestyle50Men_df.drop(free100DropMen, inplace = True)

freestyle50Men_df.to_csv('Freestyle_Men_50_First.csv')

freestyle50Women_df = graphs_df[graphs_df['Stroke'] == 'Freestyle']

freestyle50Women_df.drop(columns = ['Unnamed: 0'], inplace = True)
freestyle50Women_df.drop(columns = ['Unnamed: 0.1'], inplace = True)
freestyle50Women_df.drop(columns = ['Location'], inplace = True)
firstplaceWomenonly = freestyle50Women_df[freestyle50Women_df['Rank'] != 1].index
freestyle50Women_df.drop(firstplaceWomenonly, inplace = True)
men50Remove = freestyle50Women_df[freestyle50Women_df['Gender'] == 'Men' ].index
freestyle50Women_df.drop(men50Remove, inplace = True)
free100DropWomen = freestyle50Women_df[freestyle50Women_df['Distance (in meters)'] == '100m'].index
freestyle50Women_df.drop(free100DropWomen, inplace = True)

freestyle50Women_df.to_csv('Freestyle_Women_50_First.csv')

# Combine the two dataframes for plotting
freestyle50Men_df['Gender'] = 'Men'
freestyle50Women_df['Gender'] = 'Women'
combined50_df = pd.concat([freestyle50Men_df, freestyle50Women_df])

# Create a line plot to compare Men's and Women's Freestyle Results over the years
fig = px.line(combined50_df, x='Year', y='Results', color='Gender', title="Men's vs Women's 50m Freestyle Results Over Time", labels={'Results': 'Result', 'Year': 'Year'}, hover_data=['Gender'])
fig.write_html('Men_v_Women_Freestyle_50m_TEST.html')