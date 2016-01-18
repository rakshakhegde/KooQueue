import sqlite3
import requests
from helper import *
import time

'''
This cron_job.py is being called from a cron file located at .openshift/cron/hourly/send_msgs.cron
'''

H = int(time.strftime('%H'))
print('Hour:', H)
if not 22 <= H <= 24: # compensates for the time zone problem
	print('exiting...')
	exit()

print('Sending SMSes...')
conn = sqlite3.connect(DATA_DIR + DB_FILE_NAME)
for row in conn.execute('SELECT * FROM ' + TABLE_NAME):
	sendSms(*row)

conn.execute('DELETE FROM ' + TABLE_NAME)
conn.commit()
conn.close()