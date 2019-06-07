# importing the requests library 
import requests 
import json
  
# api-endpoint 
URL = "https://maps.googleapis.com/maps/api/directions/json"

import calendar
import time

# requires use of Universal Timezone (add 7 hours to desired PST)
# https://www.epochconverter.com/
time_getToWork = calendar.timegm(time.strptime('Jun 5, 2019 @ 15:00:00 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
time_goHome = calendar.timegm(time.strptime('Jun 6, 2019 @ 00:00:00 UTC', '%b %d, %Y @ %H:%M:%S UTC'))

print("Calculations done if you:")
print("Get to work by {}".format(time_getToWork))
print("Go home at {}".format(time_goHome))

# location given here

workAddress = {
    'Lewis': "Intel JF3, 2111 NE 25th Ave, Hillsboro, OR 97124",
    'Richards': "14325 NE Airport Way #101, Portland, OR 97230"
}

houses = {
    '1': "345 NW 88th Ave",
    '2': "216 SW Gaines St",
    '3': "3261 NW 125th Pl",
    '4': "16446 Northwest Canton Street"
}

# Heading to Work
PARAMS = {
    'origin': houses['1'],
    'destination': workAddress['Lewis'],
    'key': "AIzaSyCRgLj0qZcLc7__kbtw7rh3gtwUuIctskU",
    'arrival_time': time_goToWork
} 
  
# Heading Home
PARAMS = {
    'origin': workAddress['Lewis'],
    'destination': houses['1'],
    'key': "AIzaSyCRgLj0qZcLc7__kbtw7rh3gtwUuIctskU",
    'departure_time': time_goHome
} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 

#parsed = json.loads(data)
print(json.dumps(data, indent=4, sort_keys=True))
