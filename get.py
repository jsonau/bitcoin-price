#!/usr/bin/python
import urllib2
import json

def getJSON(url):
	return json.loads(
		urllib2.urlopen(url).read()
	)

# iterate a dictionary given a ordered list of keys and return the result
def chain_get(dictionary, ordered_keys_to_iterate):
	value = dictionary
	for key in ordered_keys_to_iterate:
		value = value.get(key)
	return value


API = [
	{
		'title': 'Coinbase',
		'url': 'https://coinbase.com/api/v1/prices/buy',
		'nodes_to_price': ['amount']
	},
	{
		'title': 'Bitstamp',
		'url': 'https://www.bitstamp.net/api/ticker/',
		'nodes_to_price': ['last']
	},
	{
		'title': 'Bitfenix',
		'url': 'https://api.bitfinex.com/v1/pubticker/BTCUSD',
		'nodes_to_price': ['last_price']
	},
	{
		'title': 'OKCoin',
		'url': 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd',
		'nodes_to_price': ['ticker', 'last']
	},
	{
		'title': 'BTC-e',
		'url': 'https://btc-e.com/api/2/btc_usd/ticker',
		'nodes_to_price': ['ticker', 'last']
	},
	{
		'title': 'itBit',
		'url': 'https://api.itbit.com/v1/markets/XBTUSD/ticker',
		'nodes_to_price': ['lastPrice']
	}
]

RESULT_TEMPLATE = " {}: {:.2f}"


for api in API:
	data = getJSON(api['url'])
	print RESULT_TEMPLATE.format(api['title'], float(chain_get(data, api['nodes_to_price'])))