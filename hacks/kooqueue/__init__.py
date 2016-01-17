import flask
import xml.etree.ElementTree as ET
import requests
from urllib.parse import unquote
import sqlite3

app = flask.Blueprint('kooqueue', __name__, template_folder='templates')

app_url = 'https://hacks-rakheg.rhcloud.com/kooqueue/'
TABLE_NAME = 'messages'
DB_FILE_NAME = 'queuedmsgs.db'

@app.route('/')
def home():
	params = flask.request.args
	try:
		phone_no = params['phone_no']
		message = unquote(params['message'])
		api_key = params['api_key']
	except Exception as e:
		print(e)
		response = ET.Element('response')
		ET.SubElement(response, 'message').text = 'phone_no, message and api_key parameters required'
		return kookooResponse(response)
	response = sendSms(phone_no, message, api_key)
	rootXML = ET.fromstring(response)
	if 'Cannot process the request before your working start hour.' in rootXML[1].text:
		queue(phone_no, message, api_key)
	return response

def queue(phone_no, message, api_key):
	import os
	data_dir = os.environ['OPENSHIFT_DATA_DIR']
	conn = sqlite3.connect(data_dir + DB_FILE_NAME)
	c = conn.cursor()
	c.execute('create table if not exists {} (phone_no text, message text, api_key text)'.format(TABLE_NAME))
	c.execute('INSERT INTO {} VALUES (?,?,?)'.format(TABLE_NAME), phone_no, message, api_key)

def sendSms(phone_no, message, api_key):
	msgUrl = 'https://www.kookoo.in/outbound/outbound_sms.php'
	payload = {'phone_no': phone_no, 'message': message, 'api_key': api_key}
	return requests.get(msgUrl, params= payload).text

def kookooResponse(ETdata):
	return xmlResponse(xmlToString(ETdata))

def xmlResponse(xmlString):
	return xmlString, 200, {'Content-Type': 'application/xml; charset=utf-8'}

def xmlToString(ETdata):
	return ET.tostring(ETdata, encoding='utf8', method='xml')

def remDbg(debugMsg):
	from datetime import datetime
	dateTimeNow = datetime.now().strftime('%y-%m-%d %H:%M:%S')
	requests.put(dbUrl + 'log/{}.json'.format(dateTimeNow), data='"{}"'.format(debugMsg))
