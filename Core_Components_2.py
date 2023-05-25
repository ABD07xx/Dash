import dash
from dash import Dash,dcc,html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Markdown('''
        #### Dash and Markdown
        # Level 1 Markdown
        ## Level 2 Markdown
        ### Level 3 Markdown
        #### Level 4 Markown 
        We can also provide text, and links as well [links](https://geeksforgeeks.org)
    ''')
            ]
        ),
        html.Div(
            children=[
                html.H4("Confirm Dialog"),
              dcc.ConfirmDialogProvider(
                    children=html.Button(
                        'Click Me',
                    ),
                    message='Do you want to continue?'
                )
            ]
        ),
        html.Div(
            children=[
                
            ]
        )
]
)




if __name__ == '__main__':
    app.run_server()