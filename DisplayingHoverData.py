import dash
from dash import Dash,html,dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import random
import json

app = dash.Dash()

# Generate random data
random.seed(42)
n_points = 50
x_values = [random.uniform(0, 10) for i in range(n_points)]
y_values = [random.uniform(0, 10) for i in range(n_points)]

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
                            'color': 'cyan',
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
        html.Pre(id='hover-data', style={'paddingTop': 35})
    ], style={'width': '30%'})
])


@app.callback(
    Output('hover-data', 'children'),
    [Input('scatter-plot', 'hoverData')])
def callback_image(hoverData):
    return json.dumps(hoverData, indent=2)


if __name__ == '__main__':
    app.run(debug=True)
