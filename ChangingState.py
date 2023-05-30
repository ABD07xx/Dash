import dash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output,State

# Create an instance of the Dash class
app = dash.Dash()

# Define the layout of the web application
app.layout = html.Div([
    dcc.Input(id='input', value='GFG', style={'fontSize': 25}),
    html.Button(id='submit', n_clicks=0, children='Submit',
                style={'fontSize': 25}),
    html.H1(id='outpt')
])

# Define a callback function that will be triggered when the submit button is clicked
@app.callback(Output('outpt', 'children'),
               [Input('submit', 'n_clicks')],
                 [State('input', 'value')])
def output(n_clicks,input_value):
    return str(input_value)

# Run the application if this file is the entry point
if __name__ == '__main__':
    app.run()
