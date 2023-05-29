import dash
from dash import Dash,dcc,html
from dash.dependencies import Input, Output
app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='id1',value='Geeks For Geeks',type='text'),
    html.Div(id='Div1')
     
])

@app.callback(Output(component_id='Div1',component_property='children'),
              [Input(component_id='id1',component_property='value')])
def update_Input(input_value):
    return "Input is :{}".format(input_value)

if __name__ == '__main__':
    app.run_server()