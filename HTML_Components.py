import dash 
import dash_html_components as html 


app = dash.Dash()
app.layout = html.Div(['Hey Geeks!!! Hello from Div 1',
                       html.Div("Hello from Div 2 (Inside Div 1)",
                       style={       
                           'color': 'Green',
                            'border': '10px Red dotted',
                            'font-family': 'Arial, sans-serif',
                            'font-size': '18px',
                            'margin-left':'35%',
                            'padding': '10px',
                            'display': 'inline-block'
                            }
                       )
                       ],
                      
                      style={       
                           'color': 'green',
                            'border': '7px orange solid',
                            'font-family': 'Arial, sans-serif',
                            'font-size': '18px',
                            'margin-left':'35%',
                            'padding': '10px',
                            'display': 'inline-block'
                            }
                      )




if __name__ == '__main__':
    app.run_server()