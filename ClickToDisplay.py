import dash
from dash import Dash,dcc,html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import random

app = dash.Dash()

def generate_random_data(n_points):
    random.seed(42)
    x_values = [random.uniform(0, 10) for _ in range(n_points)]
    y_values = [random.uniform(0, 10) for _ in range(n_points)]
    return x_values, y_values

x_values, y_values = generate_random_data(50)

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure={
                'data': [
                    go.Scatter(
                        x=x_values,
                        y=y_values,
                        mode='markers',
                        marker={
                            'size': 12,
                            'color': 'rgb(51,204,153)',
                            'line': {'width': 2}
                        }
                    )
                ],
                'layout': go.Layout(
                    title='Random Scatterplot',
                    xaxis={'title': 'X'},
                    yaxis={'title': 'Y'},
                    hovermode='closest'
                )
            }
        )
    ], style={'width': '70%', 'float': 'left'}),

    html.Div([
        html.H3(id='sum-value', style={'color': 'blue'})
    ], style={'paddingTop': 35, 'color': 'red', 'font-weight': 'bold'})
])

@app.callback(
    Output('sum-value', 'children'),
    [Input('scatter-plot', 'clickData')])
def callback_sum(clickData):
    if clickData is not None:
        point_index = clickData['points'][0]['pointIndex']
        x_value = x_values[point_index]
        y_value = y_values[point_index]
        return f'Sum: {x_value + y_value}'

    return ''
if __name__ == '__main__':
    app.run(debug=True)