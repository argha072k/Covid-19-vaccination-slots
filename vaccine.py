""" 
Developer: Arghadeep Ghosh

This program demonstrates the use case of  COWIN API (available in the public domain) to view the availability of 
vaccine type, Minimum eligible age, Available slot for a particular date and Pincode.

Check for COVID vaccine availability near you using Python | covid vaccine registration India | Python API
"""

import requests 

PINCODE = "0"
while len(PINCODE) != 6:
    PINCODE = input("Enter the pincode of the area you want to search => ")
    if len(PINCODE) < 6:
        print (f"{PINCODE} is shorter than the actual length")
    elif len(PINCODE) > 6:
        print (f"{PINCODE} is longer than the actual length")
    
REQ_DATE = input ("Enter the Date to get status (Date format: DD-MM-YYYY) => ")

request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}"
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
response = requests.get(request_link, headers = header)
raw_JSON = response.json()

Total_centers = len(raw_JSON['centers'])
print ()
print ("                        *>>>>>>    RESULTS   <<<<<<<*                                ")
print ("-------------------------------------------------------------------------------------")
print (f"Date: {REQ_DATE} | Pincode: {PINCODE} ")

if Total_centers != 0:
    print (f"Total centers in your area is: {Total_centers}" )
else:
    print (f"Unfortunately !! Seems like no center in this area ,please re-check pincode" )

print ("------------------------------------------------------------------------------------")
print ()

for i in range(Total_centers):
    print ()
    print (f"[{i+1}] Center Name:", raw_JSON['centers'][i]['name'])
    print ("------------------------------------------------------------")
    print ("   Date      Vaccine Type    Minimum Age    Available    Dose1     Dose2 ")
    print ("  ------     -------------   ------------   ----------  --------  -------- ")
    this_session = raw_JSON['centers'][i]['sessions']
    
    for j in range(len(this_session)):
        print ( "{0:^12} {1:^12} {2:^14} {3:^16} {4:^6} {4:^6}".format(this_session[j]['date'], this_session[j]['vaccine'], this_session[j]['min_age_limit'], this_session[j]['available_capacity'], this_session[j]['available_capacity_dose1'],this_session[j]['available_capacity_dose2']))