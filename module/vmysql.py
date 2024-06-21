
import mysql.connector
import json

from tabulate import tabulate

def mysqlConnect():
	db = mysql.connector.connect(
		host = "127.0.0.1",
		user = "root",
		port = "3306",
		passwd = "root",
		database = "vhacks"
	)
	return db

def mysqlQuery(query):
	db = mysqlConnect()
	dbCursor = db.cursor()
	dbCursor.execute(query)
	db.commit()
	
def mysqlFetchAll():
	db = mysqlConnect()
	dbCursor = db.cursor()
	dbCursor.execute("SELECT * FROM users")
	arrayJson = {
		"success": True,
		"data": []
	}
	for data in dbCursor.fetchall():
		arrayJson["data"].append({
			"id": data[0],
			"username": data[1],
			"email": data[2],
			"password": data[3],
			"vhc": data[4],
			"ipv4": data[5]
		})
	return json.dumps(arrayJson, indent=2)
	
def mysqlFetchOne(user, ipv4 = None):
	db = mysqlConnect()
	dbCursor = db.cursor()
	dbCursor.execute("SELECT * FROM users WHERE username = '{}' OR ipv4 = '{}'".format(user, ipv4))
	arrayJson = {
		"success": True,
		"data": []
	}
	data = dbCursor.fetchone()
	arrayJson["data"].append({
		"id": data[0],
		"username": data[1],
		"email": data[2],
		"password": data[3],
		"vhc": data[4],
		"ipv4": data[5]
	})
	return json.dumps(arrayJson, indent=2)
	
def mysqlTable(tableName):
	db = mysqlConnect()
	dbCursor = db.cursor()
	dbCursor.execute("DESCRIBE {}".format(tableName))
	arrayColumnsJson = {
		"columns": []
	}
	for columns in dbCursor.fetchall():
		arrayColumnsJson["columns"].append(columns[0])
		
	dbCursor.execute("SELECT * FROM {}".format(tableName))
	arrayDataJson = {
		"data": []
	}
	for dataUsers in dbCursor.fetchall():
		arrayDataJson["data"].append(dataUsers)
	
	header = arrayColumnsJson["columns"]
	data = arrayDataJson["data"]
	
	table = tabulate(data, header, tablefmt="psql")
	return table
