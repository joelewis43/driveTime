# libraries for API request
import requests 
import json

# libraries for time
import calendar
import time
  

def maxLength(array):
    maxLen = 0

    for i in array:
        
        temp = len(i)

        if (temp > maxLen):

            maxLen = temp
    
    return maxLen


def extend(string, newLen):

    difference = newLen - len(string)

    for i in range(0, difference):
        string += ' '

    return string






if __name__ == '__main__':

    # api-endpoint
    URL = "https://maps.googleapis.com/maps/api/directions/json"

    # requires use of Universal Timezone (add 7 hours to desired PST)
    # https://www.epochconverter.com/
    time_getToWork = calendar.timegm(time.strptime('Jul 25, 2019 @ 15:00:00 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
    time_goHome = calendar.timegm(time.strptime('Jul 26, 2019 @ 00:00:00 UTC', '%b %d, %Y @ %H:%M:%S UTC'))

    # Work addresses
    workAddress = {
        'Lewis': "Intel JF3, 2111 NE 25th Ave, Hillsboro, OR 97124",
        'Richards': "14325 NE Airport Way #101, Portland, OR 97230"
    }

    # house addresses
    houses = [
        "345 NW 88th Ave",
        "216 SW Gaines St",
        "3261 NW 125th Pl",
        "16446 NW Canton Street",
        "4246 SW Mcdonnell Terrace",
        "310 NW Brynwood Lane",
        "10572 NW Dumar Lane",
        "6044 SE Reed College Place",
    ]

    # Headers for GOING TO WORK
    WORK_PARAMS = {
        'origin': '',
        'destination': workAddress['Lewis'],
        'key': "AIzaSyCRgLj0qZcLc7__kbtw7rh3gtwUuIctskU",
        'arrival_time': time_getToWork
    } 
    
    # Headers for GOING HOME
    HOME_PARAMS = {
        'origin': '',
        'destination': '',
        'key': "AIzaSyCRgLj0qZcLc7__kbtw7rh3gtwUuIctskU",
        'departure_time': time_goHome
    } 



    maxLen = maxLength(houses)
    
    # loop over peoples work
    for person in workAddress:
        workAddr = workAddress[person]

        print("{}'s Times".format(person))
        print("House Address\t\tShort Time\tLong Time\t")
        print("_______________________________________________________________________________")

        # loop over houses - Heading Home
        for house in houses:

            # add the house the the headers
            HOME_PARAMS['destination'] = house
            HOME_PARAMS['origin'] = workAddr

            # sending get request and saving the response as response object 
            r = requests.get(url = URL, params = HOME_PARAMS) 
        
            # extracting data in json format 
            data = r.json() 

            time_short = data['routes'][0]['legs'][0]['duration']['text']
            time_long = data['routes'][0]['legs'][0]['duration_in_traffic']['text']

            house = extend(house, maxLen)

            print("{}\t{}\t\t{}".format(house, time_short, time_long))

        print("\n\n")