import gspread

from oauth2client.service_account import ServiceAccountCredentials

# Log in to the spreadsheet
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("Public IP").sheet1

# Read the spreadsheet
ip = wks.acell('A2').value

# Save the value to a file
with open('ip.txt', 'w') as file:
    file.write(ip)
