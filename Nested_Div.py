import dash 
from dash import Dash,html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H4("Geeks")
            ]
        ),
        html.Div(
            children=[
                html.H4("For")
            ]
        ),
        html.Div(
            children=[
                html.H4("Geeks")
            ]
        )
    ]
)



if __name__ == '__main__':
    app.run_server()