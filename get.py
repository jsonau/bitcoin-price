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
		'title': 'BitStamp',
		'url': 'https://www.bitstamp.net/api/ticker/',
		'nodes_to_price': ['last']
	},
	{
		'title': 'BTC-e',
		'url': 'https://btc-e.com/api/2/btc_usd/ticker',
		'nodes_to_price': ['ticker', 'last']
	},
]

RESULT_TEMPLATE = " {}: {}"


for api in API:
	data = getJSON(api['url'])
	print RESULT_TEMPLATE.format(api['title'], chain_get(data, api['nodes_to_price']))