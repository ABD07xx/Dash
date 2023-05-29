import dash
from dash import html,dcc,Dash
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('mpg.csv')

app = dash.Dash()

#list of columns
fts = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',options=[{'label':i,'value':i} for i in fts],
                     value='displacement')
    ],style={'width':'45%','display':'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',options=[{'label':i,'value':i} for i in fts],
                     value='acceleration')
    ],style={'width':'45%','display':'inline-block'}),
    dcc.Graph(id='graph' )
])
@app.callback(Output('graph', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
def call_graph(xaxisname, yaxisname):
    return {
        'data': [go.Scatter(
            x=df[xaxisname],
            y=df[yaxisname],
            text=df['name'],
            mode='markers',
            opacity=0.5,
            line={'width': 0.5, 'color': 'black'}
        )],
        'layout': go.Layout(
            title='Dashboard MPG',
            xaxis={'title': xaxisname},
            yaxis={'title': yaxisname},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run(debug=True)
