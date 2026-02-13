import pandas as pd
import yfinance as yf
from datetime import datetime



def convert_to_date(date_):
	date_ = date_.split(' ')[0]
	date_ = datetime.strptime(date_, '%Y-%m-%d')
	# date_ = datetime.strptime(date_, '%d-%m-%Y')
	return date_


def roundDigits(value):
	if pd.notnull(value):
		value = round(value, 2)
	if pd.isnull(value):
		return None
	return value


def change_format(date_):
	date_ = datetime.strptime(date_, '%m/%d/%Y')
	date_ = datetime.strftime(date_, '%Y-%m-%d')
	return date_





def collectYahoo(ticker):
	if ticker = 'gold':
		tick = yf.Ticker("GC=F")
	if ticker = 'snp':
		tick = yf.Ticker("^GSPC")

	data = tick.history(period="max")
	pd.set_option('display.max_rows', None) 
	return data



def processData(dataF):
	dataF['Date'] = dataF['Date'].apply(convert_to_date)

	datedf = pd.date_range(start='1927-12-30', end='2025-12-22')
	datedf = pd.DataFrame(datedf, columns=['full date'])

	dataF = datedf.merge(dataF, left_on=['full date'], right_on=['Date'], how='left')

	dataF['Open'] = dataF['Open'].apply(roundDigits)
	dataF['High'] = dataF['High'].apply(roundDigits)
	dataF['Low'] = dataF['Low'].apply(roundDigits)
	dataF['Close'] = dataF['Close'].apply(roundDigits)

	return dataF




if __name__ == "__main__":

	golddf = collectYahoo('gold')
	golddf = processData(golddf)
	golddf.to_csv('goldPrices.csv', index=False)


	snpdf = collectYahoo('snp')
	snpdf = processData(snpdf)
	snpdf.to_csv('snp500.csv', index=False)