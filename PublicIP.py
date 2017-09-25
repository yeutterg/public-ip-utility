import getip
import gspread
import time

from oauth2client.service_account import ServiceAccountCredentials

# Get the public IP address
ip = getip.get()

# Get the local time
localtime = time.asctime(time.localtime(time.time()))

# Log in to the spreadsheet
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("Public IP").sheet1

# Update the spreadsheet
wks.update_acell('A2', ip)
wks.update_acell('B2', localtime)
