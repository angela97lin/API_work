import urllib2
import json

###The Directions API may only be used in conjunction with displaying results on a Google map; using Directions data without displaying a map for which directions data was requested is prohibited.

##GOOGLE API KEY
key = 'AIzaSyBun2m9jaQTFGb0qtR7Shh7inqFhzKbLL4'

if __name__ == '__main__':
        ########################################
        ##CITIBIKE INFO:
        url = "http://www.citibikenyc.com/stations/json"
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result) #dictionary of our results (tuples?)
        #print d
        execTime = d['executionTime'] #gets the time when program was run, keeping here in case we want to use that somewhere!
        #just for testing purposes...
	rlist = d['stationBeanList']
	for r in rlist:
		print r['stationName'] 
        #######################################
        ##GOOGLE INFO:
        #example: from Montreal to Toronto
        googleurl = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=%s" % (key)
        #print googleurl
        request = urllib2.urlopen(googleurl)
        results = request.read()
        gd = json.loads(results) #dictionary of results returned by google
        routes = gd['routes']
        #NOTE: routes is a value in the dictionary gd; it is also a list with one element
        #legs is the zeroth element of the routes list... and is itself another list
        legs = routes[0]['legs']
        #distance is referrring to the dictionary 'distance' in the first element of the list legs (which is a dictionary itself and where once again, all our valuable info is)
        distance = legs[0]['distance']
        print distance['text'] #returns textual information about distance btwn two points
        print distance['value']#I actually have NO idea what this refers to
