import dash
from dash import dcc,html,Dash

app = dash.Dash()

app.layout = html.Div(children=[
                        html.H1("Hello Geeks!!"),
                        html.Div("This is a nested Div")         
                    ])

if __name__ == '__main__':
    app.run_server()


