import dash
from dash import dcc,html,Dash

app = dash.Dash()
data = [
        #Creating a dictionary to be displayed as bar plot
        {'x':[1,3,5],'y':[2,4,7],'type':'bar','name':'Plot'},
        {'x':[1.5,3.5,5.5],'y':[3,5,8],'type':'bar','name':'Plot2'},
        {'x':[2,4,6],'y':[4,6,9],'type':'bar','name':'Plot3'}
        ]

colors = {'background':'#111111','text':'#7FDBFF'}

app.layout = html.Div(children=[

             html.H1('Hello Geeks!!!',
                     style={'textAlign':'center',
                     'color':colors['text']}),


            dcc.Graph(id='example',
                        figure={'data':data,
                                
                                'layout': {
                                    'plot_bgcolor':colors['background'],
                                    'paper_bgcolor':colors['background'],
                                    'font':{'color':colors['text']},
                                    'title':"First Bar Plots using Dash"
                                }})      
        ],style={'backgroundColor':colors['background']}
        
        )
if __name__ == '__main__':
    app.run_server()