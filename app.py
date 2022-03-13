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
SAMPLE_SPREADSHEET_ID = '1yNF_F7cLnsIWfTJ6gncb9ty_NMo039PStsxPmo2i1oo'
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
	sheetID = data["sheetID"]
	sheetRange = data["sheetRange"]
	sheetValues = data["sheetValues"]
	sheetDump = json.dumps(sheetValues)
	sheetValues = json.loads(sheetDump)

	#Gets Data before appending 
	sheetread = sheet.values().get(spreadsheetId=sheetID,range=sheetRange).execute()
	values = sheetread.get('values',[])
	
	if not values:
		print('UNINITIALIZED LIST')
		#write the values as is
		for i in range(len(sheetValues)):
			sheetValues[i][0] = "="+sheetValues[i][0]

		requests = sheet.values().update(spreadsheetId=sheetID,range=sheetRange,valueInputOption="USER_ENTERED",body={"values": sheetValues}).execute()
		print(requests)

	else:
		for i in range(len(values)):
			if values[i][0]!="":
				values[i][0] = "="+values[i][0]+"+"+sheetValues[i][0]
			else:
				values[i][0] = "="+sheetValues[i][0]

			print(values[i][0])
		
		print(values)
		requests = sheet.values().update(spreadsheetId=sheetID,range=sheetRange,valueInputOption="USER_ENTERED",body={"values": values}).execute()

	result = {"result": requests}
	return jsonify(result)	
