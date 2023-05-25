import dash
from dash import Dash,html,dcc

app = dash.Dash()

# Define CSS styles
styles = {
    'container': {
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'margin-top': '50px',
        'background-color': '#F4F4F4',
        'padding': '20px',
    },
    'header': {
        'text-align': 'center',
        'color': 'black',
        'border': '7px solid black',
        'padding': '20px',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
    },
    'content': {
        'text-align': 'center',
        'color': 'blue',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
    },
    'dropdown': {
        'text-align': 'center',
        'color': 'black',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
    },
    'selected_dropdown': {
        'text-align': 'center',
        'color': 'green',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
    },
    'input': {
        'text-align': 'center',
        'color': 'black',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
    },
    'textarea': {
        'text-align': 'center',
        'color': 'black',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
    },
    'slider': {
        'text-align': 'center',
        'color': 'black',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
        'width': '70%',
        'margin-left': '15%',
    },
    'buttons': {
        'text-align': 'center',
        'color': 'black',
        'margin-bottom': '30px',
        'background-color': '#FFFFFF',
        'padding': '20px',
    },
}

app.layout = html.Div(
    children=[
        #Text/Para/Headers
        html.Div(
            children=[
                html.H1("Texts/Paragraphs/Headers")
            ],
            style=styles['header']
        ),

        html.Div(
            children=[
                html.H1("Welcome to My Web App Header 1"),
                html.H2("Another section in Header 2"),
                html.H3("Another section in H3"),
                html.P("This is a sample paragraph."),
                html.Div("Writing inside a div")
            ],
            style=styles['content']
        ),

        # Dropdown
        html.Div(
            children=[
                html.H1("Dropdowns in DASH"),
                dcc.Dropdown(options=['Delhi', 'Mumbai', 'Chennai', 'Punjab']),
            ],
            style=styles['dropdown']
        ),

        html.Div(
            children=[
                html.H3("Pre Selected Value"),
                dcc.Dropdown(options=['Delhi', 'Mumbai', 'Chennai', 'Punjab'], value='Mumbai'),
            ],
            style=styles['selected_dropdown']
        ),

        html.Div(
            children=[
                html.H3("MultiSelect"),
                dcc.Dropdown(options=['Delhi', 'Mumbai', 'Chennai', 'Punjab'], multi=True),
            ],
            style=styles['selected_dropdown']
        ),

        # Input
        html.Div(
            children=[
                html.H3("Input Text"),
                dcc.Input(type='text', placeholder='Enter text', value=''),
            ],
            style=styles['input']
        ),

        # Text Area
        html.Div(
            children=[
                html.H3("Text Area"),
                dcc.Textarea(
                    placeholder='Enter text',
                    value='',
                    style={'width': '100%'}
                ),
            ],
            style=styles['textarea']
        ),

        # Slider
        html.Div(
            children=[
                html.H3("Slider"),
                dcc.Slider(min=0, max=10, step=1, value=5),
            ],
            style=styles['slider']
        ),

        # Range Slider
        html.Div(
            children=[
                html.H3("Range Slider"),
                dcc.RangeSlider(min=0, max=10, step=1, value=[3, 7]),
            ],
            style=styles['slider']
        ),

        # Checkboxes
        html.Div(
            children=[
                html.H3("Checkboxes"),
                dcc.Checklist(
                    options=[
                        {'label': 'Option 1', 'value': 'option1'},
                        {'label': 'Option 2', 'value': 'option2'},
                        {'label': 'Option 3', 'value': 'option3'}
                    ],
                    value=['option1']
                ),
            ],
            style=styles['content']
        ),

        # Radio buttons
        html.Div(
            children=[
                html.H3("Radio Buttons"),
                dcc.RadioItems(
                    options=[
                        {'label': 'Option 1', 'value': 'option1'},
                        {'label': 'Option 2', 'value': 'option2'},
                        {'label': 'Option 3', 'value': 'option3'}
                    ],
                    value='option1'
                ),
            ],
            style=styles['content']
        ),

        # Buttons
        html.Div(
            children=[
                html.H3("Buttons"),
                html.Button('Button 1', id='button-1'),
                html.Button('Button 2', id='button-2'),
            ],
            style=styles['buttons']
        ),
    ],
    style=styles['container']
)

if __name__ == '__main__':
    app.run_server()
