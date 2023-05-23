import dash
from dash import dcc,html,Dash

app = dash.Dash()

app.layout = html.Div(children=[
            dcc.Graph(id='example',
                        figure={'data':[
                            #Creating a dictionary to be displayed as bar plot
                            {'x':[1,3,5],'y':[2,4,7],'type':'bar','name':'Plot'},
                            {'x':[1.5,3.5,5.5],'y':[3,5,8],'type':'bar','name':'Plot2'},
                            {'x':[2,4,6],'y':[4,6,9],'type':'bar','name':'Plot3'}
                        ],
                                'layout': {
                                    'title':"First Bar Plots using Dash"
                                }})      
        ])
if __name__ == '__main__':
    app.run_server()


