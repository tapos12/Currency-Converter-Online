from flask import Flask
from flask import request
import urllib3
import xmltodict
from datetime import date, datetime, timedelta
import json
import pickle

app = Flask(__name__)


@app.route('/convert')
def convert():
	amount = request.args.get('amount', default = 1, type = float)
	src_currency = request.args.get('src_currency', default = 'EUR', type = str)
	dest_currency = request.args.get('dest_currency', default = 'EUR', type = str)
	reference_date = request.args.get('reference_date', default = '2020-03-20', type = int)
	json = convertCurr(amount, src_currency, dest_currency, reference_date)
	return json


def fetchData():
	"""
	Fetch data from the exchange rates xml link and return the rates in dictionary
	"""

	myLink = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
	currency_dictionary = {}
	http = urllib3.PoolManager()
	response = http.request('GET', myLink)
	data = xmltodict.parse(response.data)
	#pprint(data)
	for k, v in data.items():
		for k2, v2 in v.items():
			if k2=='Cube':
				for kc, vc in v2.items():
					#print(kc)
					for vv in vc:
						for key1, layer1 in vv.items():
							if key1=='@time' and layer1 not in currency_dictionary:
								curr_time = layer1
								currency_dictionary[curr_time] = {}
							if key1=='Cube':
								for l in layer1:
									for llk, llv in l.items():
										if llk=='@currency': cur=llv
										if llk=='@rate': rate=llv
									if cur and rate:
										currency_dictionary[curr_time][cur]=rate
										cur = ''
										rate = ''
	return currency_dictionary

def convertCurr(amount, src, dest, date):
	"""
	Convert the currency amount here, given the amount, source, destination and date information
	If yesterday's date is not found in the existing saved dictionary, currency information are fetched from the link
	"""
	try:
		pickle_in = open('saved_currency.pickle','rb')
		currency_dictionary = pickle.load(pickle_in)
		yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
		if yesterday not in currency_dictionary:
			currency_dictionary = fetchData()
			pickle_out = open('saved_currency.pickle', 'wb')
			pickle.dump(currency_dictionary, pickle_out)
	except:
		currency_dictionary = fetchData()
		pickle_out = open('saved_currency.pickle', 'wb')
		pickle.dump(currency_dictionary, pickle_out)
	try:
		if src != 'EUR' and dest != 'EUR':
			result =  (1/float(currency_dictionary[date][src])) * (float(currency_dictionary[date][dest])) * amount
		if src == 'EUR':
			result = float(currency_dictionary[date][dest]) * amount
		if dest == 'EUR':
			result = (1/float(currency_dictionary[date][src])) * amount
		
		x = {"amount": result, "currency": dest}
		return json.dumps(x)
	except:
		return 'Please provide valid information'

if __name__ == '__main__':
    app.run()