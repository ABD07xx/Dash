import dash
from dash import Dash,html

app = dash.Dash()

refresh_click = 0
def updating_layout():
    global refresh_click
    refresh_click += 1
    return html.H1('Refresh button clicked {} times'.format(refresh_click))

app.layout = updating_layout

if __name__ == '__main__':
    app.run_server()