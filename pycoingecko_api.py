from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
bitcoin_price_data = bitcoin_data['prices']
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])

data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

candle_stick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

candle_stick_data.to_csv('bitcoin_price_data.csv')