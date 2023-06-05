import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

cryptocurrencies = [
    {'label': 'Bitcoin', 'value': 'bitcoin'}
    # Add more cryptocurrencies as needed
]

app.layout = html.Div([
    html.H1("Cryptocurrency Price Tracker"),
    dcc.Dropdown(
        id='crypto-dropdown',
        options=cryptocurrencies,
        multi=True,
        value=['bitcoin'],  # Initial selection
    ),
    dcc.Graph(id='price-graph'),
    html.Div(id='price-info'),
    dcc.Interval(
        id='interval-component',
        interval=1000*60,  # Update every 1 minute (60 seconds)
        n_intervals=0
    )
])

def get_price_info(cryptos):
    # Use symbol parameter instead of value parameter
    ids = ','.join(crypto['symbol'] for crypto in cryptos)
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={ids}"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'f49a0a67-cd01-433f-bfba-7b0e867d0109'  # Replace with your CoinMarketCap API key
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinMarketCap API: {e}")
        return None

@app.callback(
    Output('price-graph', 'figure'),
    Output('price-info', 'children'),
    [Input('crypto-dropdown', 'value')],
    [Input('interval-component', 'n_intervals')]
)
def update_price_info(cryptos, n):
    if not cryptos:
        return {}, ""

    price_data = get_price_info(cryptos)
    if price_data is None:
        return {}, "Error fetching data from API. Please try again later."

    try:
        # Use list comprehension instead of for loop to create data list
        data = [go.Scatter(
            x=pd.to_datetime(timestamps[crypto['symbol']], unit='ms'),
            y=prices[crypto['symbol']],
            mode='lines',
            name=crypto['label']
        ) for crypto in cryptos]

        price_list = []
        for crypto in cryptos:
            crypto_name = crypto['label']
            crypto_id = crypto['value']

            if crypto_id in price_data['data']:
                crypto_info = price_data['data'][crypto_id]
                latest_price = crypto_info['quote']['USD']['price']
                price_list.append(html.P(f"{crypto_name}: ${latest_price:.2f}"))

        layout = go.Layout(
            title='Cryptocurrency Price Trends',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Price (USD)'),
            showlegend=True,
            legend=dict(orientation='h')
        )

        return {'data': data, 'layout': layout}, price_list
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run_server()
