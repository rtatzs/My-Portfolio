import json
from optparse import Values
from re import I

from myprofilelib.profile import getInitializeProfile
from pickle import NONE, TRUE
from flask import Flask, render_template, request, flash, jsonify

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = Flask(__name__)
app.secret_key = "f5bb0c8de146c67b44babbf4e6584cc0"

SERVICE_ACCOUNT_FILE = "static/files/2c9c9cd97be2e079377d9dfb6c1139d8.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = ''
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()

@app.route("/MyProfile")
def myprofile():
	myprofile = getInitializeProfile()
	return render_template("myprofile.html", myprofile = myprofile)

@app.route("/readsheet")
def GoogleSheetRead():
	sheetID = request.args.get('SheetID', default='',type=str)
	sheetRange = request.args.get('SheetRange', default='',type=str)
	sheetread = sheet.values().get(spreadsheetId=sheetID,range=sheetRange).execute()
	values = sheetread.get('values',[])
	result = {"result": values}
	return jsonify(result)

@app.route("/writesheet",methods=['POST'])
def GoogleSheetWrite():
	data = json.loads(request.data.decode())
	sheetID = data["sheetID"]
	sheetRange = data["sheetRange"]
	sheetValues = data["sheetValues"]
	sheetDump = json.dumps(sheetValues)
	sheetValues = json.loads(sheetDump)
	requests = sheet.values().update(spreadsheetId=sheetID,
                                 	range=sheetRange,
                                 	valueInputOption="USER_ENTERED",
                                 	body={"values": sheetValues}).execute()
	result = {"result": requests}
	return jsonify(result)	

@app.route("/append", methods=['POST'])
def GoogleSheetAppend():
	data = json.loads(request.data.decode())
	transDate = data["instaDate"]
	sheetID = data["sheetID"]
	sheetRange = data["sheetRange"]
	sheetValues = data["sheetValues"]
	sheetDump = json.dumps(sheetValues)
	sheetValues = json.loads(sheetDump)


	index = IdentifyQuencena(transDate,'2023')
	print(transDate)
	print(index)

	#Gets Data before appending 
	sheetread = sheet.values().get(spreadsheetId=sheetID,range=sheetRange).execute()
	values = sheetread.get('values',[])
	
	if not values:
		# print('UNINITIALIZED LIST')
		#write the values e.g. (=24)
		for i in range(len(sheetValues)):
			sheetValues[i][0] = "="+sheetValues[i][0]

		requests = sheet.values().update(spreadsheetId=sheetID,range=sheetRange,valueInputOption="USER_ENTERED",body={"values": sheetValues}).execute()
		# print(requests)

	else:
		#write values e.g. (=24+2)
		for i in range(len(values)):
			if values[i][0]!="":
				values[i][0] = "="+values[i][0]+"+"+sheetValues[i][0]
			else:
				values[i][0] = "="+sheetValues[i][0]

			# print(values[i][0])
		
		print(values)
		requests = sheet.values().update(spreadsheetId=sheetID,range=sheetRange,valueInputOption="USER_ENTERED",body={"values": values}).execute()

	result = {"result": requests}
	return jsonify(result)	

@app.route("/addExpense",methods=['POST'])
def appendExpense():

	data = json.loads(request.data.decode())    #Decode JSON Parameters
	transDate = data["instaDate"]       	    #Transcation Date
	sheetID = data["sheetID"]				    #Google Sheet ID
	sheetRange = data["sheetRange"]     	    #Probably not needed
	sheetValues = data["sheetValues"]   	    #Expense as JSON Array
	sheetDump = json.dumps(sheetValues) 	    #Dumped JSON Array
	sheetValues = json.loads(sheetDump) 		#Expenses Array
	column = IdentifyQuencena(transDate,'2023') #Identify the Column
	
	print(data)

	#Foreach expense
	for i in range(len(sheetValues)):
		
		#identify cell location in google sheets
		column = IdentifyQuencena(transDate,'2023')
		row = IdentifyExpenseType(sheetValues[i]['Remarks'])
		cell = "Budget!"+column+row
		
		#get param expense value
		amount = sheetValues[i]['Amount']

		#read current cell content
		sheetread = sheet.values().get(spreadsheetId=sheetID,range=cell).execute()
		values = sheetread.get('values',[])
		
		#If cell is uninitialized, initialize
		if not values:
			tmp = []
			tmp.append("="+amount)
			values.append(tmp)
		#if cell is not empty concat with plus
		elif values[0][0]!="":
			#includes comma removal
			values[0][0] = "="+values[0][0].replace(",","")+"+"+amount
		#if cell is empty directly assign
		else:
			values[0][0] = "="+amount
		
		#write the new cell value
		requests = sheet.values().update(spreadsheetId=sheetID,range=cell,valueInputOption="USER_ENTERED",body={"values": values}).execute()		
	
	result = {"result":requests}
	return jsonify(result)	

def IdentifyExpenseType(expense_type):
	row = '28'
	if expense_type == 'Electric':
		row = '28'
	elif expense_type == 'Internet':
		row = '29'
	elif expense_type == 'LPG':
		row = '30'
	elif expense_type == 'Water':
		row = '31'
	elif expense_type == 'Manulife':
		row = '32'
	elif expense_type == 'Housing':
		row = '33'
	elif expense_type == 'Parents':
		row = '34'
	elif expense_type == 'Tithes':
		row = '35'
	elif expense_type == 'Mass':
		row = '36'
	elif expense_type == 'Work Meal':
		row = '37'
	elif expense_type == 'House(Tax)':
		row = '38'
	elif expense_type == 'House(Maintain)':
		row = '39'
	elif expense_type == 'Transpo(Maintain)':
		row = '40'
	elif expense_type == 'Transpo(Gas)':
		row = '41'
	elif expense_type == 'WorkSnack':
		row = '42'
	elif expense_type == 'Hygenic':
		row = '50'
	elif expense_type == 'Vitamins':
		row = '51'
	elif expense_type == 'Groceries':
		row = '52'
	elif expense_type == 'Other Food':
		row = '53'
	elif expense_type == 'Career':
		row = '57'
	elif expense_type == 'Investments':
		row = '58'
	elif expense_type == 'Donation':
		row = '59'
	elif expense_type == 'Leisure':
		row = '60'		
	elif expense_type == 'Buy Online':
		row = '61'
	elif expense_type == 'Planned':
		row = '62'
	elif expense_type == 'Others':
		row = '63'
	elif expense_type == 'Pet':
		row = '64'
	elif expense_type == 'Hobby':
		row = '65'

	return row	

def IdentifyQuencena(date,year):
	index = 'C'
	if date >= year+'-01-01' and date <= year+'-01-15':
		index = 'C'
	elif date >= year+'-01-16' and date <= year+'-01-31':
		index = 'D'
	elif date >= year+'-02-01' and date <= year+'-02-15':
		index = 'E'
	elif date >= year+'-02-16' and date <= year+'-02-28':
		index = 'F'
	elif date >= year+'-03-01' and date <= year+'-03-15':
		index = 'G'
	elif date >= year+'-03-16' and date <= year+'-03-31':
		index = 'H'
	elif date >= year+'-04-01' and date <= year+'-04-15':
		index = 'I'
	elif date >= year+'-04-16' and date <= year+'-04-30':
		index = 'J'
	elif date >= year+'-05-01' and date <= year+'-05-15':
		index = 'K'
	elif date >= year+'-05-16' and date <= year+'-05-31':
		index = 'L'
	elif date >= year+'-06-01' and date <= year+'-06-15':
		index = 'M'
	elif date >= year+'-06-16' and date <= year+'-06-30':
		index = 'N'
	elif date >= year+'-07-01' and date <= year+'-07-15':
		index = 'O'
	elif date >= year+'-07-16' and date <= year+'-07-31':
		index = 'P'
	elif date >= year+'-08-01' and date <= year+'-08-15':
		index = 'Q'
	elif date >= year+'-08-16' and date <= year+'-08-31':
		index = 'R'
	elif date >= year+'-09-01' and date <= year+'-09-15':
		index = 'S'
	elif date >= year+'-09-16' and date <= year+'-09-30':
		index = 'T'
	elif date >= year+'-10-01' and date <= year+'-10-15':
		index = 'U'
	elif date >= year+'-10-16' and date <= year+'-10-31':
		index = 'V'
	elif date >= year+'-11-01' and date <= year+'-11-15':
		index = 'W'
	elif date >= year+'-11-16' and date <= year+'-11-30':
		index = 'X'
	elif date >= year+'-12-01' and date <= year+'-12-15':
		index = 'Y'
	elif date >= year+'-12-16' and date <= year+'-12-31':
		index = 'Z'
								
	return index
