import dash
from dash import html,dcc,Dash
from dash.dependencies import Input, Output

app = dash.Dash()


app.layout = html.Div([
    html.H1("Multiple Inputs and Outputs"),
    html.Div([
        html.Label("Input 1"),
        dcc.Input(id="input-1", type="text", value=""),
    ]),
    html.Div([
        html.Label("Input 2"),
        dcc.Input(id="input-2", type="text", value=""),
    ]),
    html.Div([
        html.Label("Input 3"),
        dcc.Input(id="input-3", type="text", value=""),
    ]),
    html.Div(id="output-container"),
    html.Div(id="concatenated-output")
])

@app.callback(
    Output("output-container", "children"),
    [Input("input-1", "value"),
     Input("input-2", "value"),
     Input("input-3", "value")]
)
def update_output(input1, input2, input3):
    if input1 and input2 and input3:
        # Output for all inputs provided
        return html.Div([
            html.H3("Output for All Inputs"),
            html.Div(f"Input 1: {input1}"),
            html.Div(f"Input 2: {input2}"),
            html.Div(f"Input 3: {input3}")
        ])
    else:
        # No output if not enough inputs provided
        return ""

@app.callback(
    Output("concatenated-output", "children"),
    [Input("input-1", "value"),
     Input("input-2", "value"),
     Input("input-3", "value")]
)
def concatenate_inputs(input1, input2, input3):
    if input1 and input2 and input3:
        # Concatenate all inputs
        concatenated = input1 + input2 + input3
        return html.Div([
            html.H3("Concatenated Output"),
            html.Div(f"Concatenated: {concatenated}")
        ])
    else:
        # No output if not enough inputs provided
        return ""

if __name__ == "__main__":
    app.run_server(debug=True)
