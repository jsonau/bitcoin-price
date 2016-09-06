#!/usr/bin/python

import urllib2
import json

def getJSON(url):
	return json.loads(
		urllib2.urlopen(url).read()
	)

template = " {}: {}"

data = getJSON("https://coinbase.com/api/v1/prices/buy")
print template.format( 'Coinbase', data['amount'])

data = getJSON("https://www.bitstamp.net/api/ticker/")
print template.format( 'BitStamp', data['last'])

data = getJSON("https://btc-e.com/api/2/btc_usd/ticker")
print template.format( "BTC-e", data['ticker']['last'])
