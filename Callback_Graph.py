import dash
from dash import Dash,html,dcc 
from dash.dependencies import Input,Output

import plotly.graph_objs as go
import pandas as pd

#Data about per capita income of various countries 
df = pd.read_csv("gapminderDataFiveYear.csv")

app = dash.Dash()

year_options = []
for year in df['year'].unique():
 year_options.append({'label':str(year),'value':year})

app.layout = html.Div([
 #graph
 dcc.Graph(id='Graph'),
 #Dropdown
 dcc.Dropdown(id='Dropdown',options=year_options,
 value=df['year'].min(),style={'width':'50%','margin':'auto', 'border':'solid black'})
])

#Fucntion to connect the dropdown to actual graph

@app.callback(Output('Graph','figure'),[Input('Dropdown','value')])
def update_graph(selected_year):
 
 #Selected Year's data
 filtered_df = df[df['year'] == selected_year]
 
 #Data for a continent like data for Asia and creating a plot for them
 plot = []
 for filtered_continent in filtered_df['continent'].unique():
    df_continent = filtered_df[filtered_df['continent'] == filtered_continent]
    plot.append(go.Scatter(
    x=df_continent['gdpPercap'],
    y=df_continent['lifeExp'],
    mode='markers',
    opacity= 0.8,
    marker = {'size':15},
    name = filtered_continent
 ))
 
 
 return {'data': plot,'layout':go.Layout(title="Scatter Plot",
 xaxis={'title':'GDP per capita','type':'log'},
 yaxis={'title':'Life Expectancy'})} 


if __name__ == '__main__':
 app.run_server(debug=True)
