import psycopg2
import pandas as pd
import psycopg2.extras
import numpy as np
import time



conn_details = psycopg2.connect(
	host="localhost",
	database="resourcesTracker",
	user="postgres",
	password="JVKMarg",
	port= "5432"
)



cursor = conn_details.cursor()


def createGoldUSDTable():
	sql_query = '''CREATE TABLE goldpricesusd
		(
			priceDate date NOT NULL PRIMARY KEY,
			openPrice NUMERIC(6,2),
			highPrice NUMERIC(6,2),
			lowPrice NUMERIC(6,2),
			closePrice NUMERIC(6,2),
			source VARCHAR(10)
			)'''
	cursor.execute(sql_query)
	conn_details.commit()
	cursor.close()
	conn_details.close()



def insertGoldUSDfromCSV():
	df = pd.read_csv(r"goldPrices.csv")

	df = df.replace({np.nan: None})
	
	for index, row in df.iterrows():
		
		date_ = row['date']
		openPrice = row['open']
		highPrice = row['high']
		lowPrice = row['low']
		closePrice = row['close']
		source = row['source']

		docSingle = (date_, openPrice, highPrice, lowPrice, closePrice, source)

		sql_query = '''INSERT INTO goldpricesusd VALUES(%s, %s, %s, %s, %s, %s)'''


		cursor.execute(sql_query, docSingle)

		if index%1000 == 0:
			print(index)
			conn_details.commit()
	conn_details.commit()
	cursor.close()
	conn_details.close()




def createsnp500Table():
	sql_query = '''CREATE TABLE snp500
		(
			priceDate date NOT NULL PRIMARY KEY,
			openPrice NUMERIC(6,2),
			highPrice NUMERIC(6,2),
			lowPrice NUMERIC(6,2),
			closePrice NUMERIC(6,2)
			)'''
	cursor.execute(sql_query)
	conn_details.commit()
	cursor.close()
	conn_details.close()




def insertsnp500fromCSV():
	df = pd.read_csv(r"snp500Prices.csv")

	df = df.replace({np.nan: None})
	
	for index, row in df.iterrows():
		
		date_ = row['date']
		openPrice = row['open']
		highPrice = row['high']
		lowPrice = row['low']
		closePrice = row['close']

		docSingle = (date_, openPrice, highPrice, lowPrice, closePrice)

		sql_query = '''INSERT INTO snp500 VALUES(%s, %s, %s, %s, %s)'''


		cursor.execute(sql_query, docSingle)

		if index%1000 == 0:
			print(index)
			conn_details.commit()
	conn_details.commit()
	cursor.close()
	conn_details.close()




if __name__ == "__main__":
	# createGoldUSDTable()
	time.sleep(10)
	# insertGoldUSDfromCSV()

	time.sleep(10)

	# createsnp500Table()
	time.sleep(10)
	# insertsnp500fromCSV()