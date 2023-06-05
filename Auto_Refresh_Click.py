import dash
from dash import Dash,html,dcc
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([
    html.H1(id='live_update'),
    dcc.Interval(id='interval',
                 interval=5000,
                 n_intervals=0)
])

@app.callback(Output('live_update','children'),
              [Input('interval','n_intervals')])
def update_layout(n):
    return "Page Refreshed {} times".format(n)



if __name__ == '__main__':
    app.run_server()