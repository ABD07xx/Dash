import dash
from dash import Dash, html, dcc

# Plotly libs
import plotly.graph_objs as go

# To create random dataset
import numpy as np

data = [
    # Creating a dictionary to be displayed as bar plot
    {'x': [1, 3, 5], 'y': [2, 4, 7], 'type': 'bar', 'name': 'Plot'},
    {'x': [1.5, 3.5, 5.5], 'y': [3, 5, 8], 'type': 'bar', 'name': 'Plot2'},
    {'x': [2, 4, 6], 'y': [4, 6, 9], 'type': 'bar', 'name': 'Plot3'}
]

app = dash.Dash()
np.random.seed(0)
random_x = np.random.randint(1, 501, 100)
random_y = np.random.randint(1, 501, 100)

# Graph
app.layout = html.Div([
    dcc.Graph(
        id='Plotly_ScatterPlot',
        figure={
            'data': [go.Scatter(x=random_x, y=random_y, mode='markers',
                                marker={
                                    'size': 12,
                                    'color': 'blue',
                                    'symbol': 'diamond',
                                    'line': {'width': 2}
                                })],
            'layout': go.Layout(title='Scatter Plot',
                                xaxis={'title': 'X Axis'},
                                yaxis={'title': 'Y Axis'})
        }
    ),
    # Second Plot inside Separate Div
    html.Div([
        dcc.Graph(
            id='Bar_Plot',
            figure={
                'data': data,
                'layout': {
                    'title': "Bar Plot"
                }
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server()
