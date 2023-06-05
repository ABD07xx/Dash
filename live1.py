import dash
from dash import html,dcc,html
import requests

api_url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"

app = dash.Dash()

def get_flight_data():
    res = requests.get(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    return counter

app.layout = html.Div([
    html.Div([
        html.H3('Flight Radar Data'),
        html.Div(id='flight-counter')
    ]),
    dcc.Interval(id='interval-component', interval=5000, n_intervals=0)
])


@app.callback(
    dash.dependencies.Output('flight-counter', 'children'),
    dash.dependencies.Input('interval-component', 'n_intervals')
)
def update_flight_data(n):
    counter = get_flight_data()
    return f'Active flights worldwide: {counter}'

if __name__ == '__main__':
    app.run_server(debug=True)
