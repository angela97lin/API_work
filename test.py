import urllib2
import json

###The Directions API may only be used in conjunction with displaying results on a Google map; using Directions data without displaying a map for which directions data was requested is prohibited.

##COMPARING CITI-BIKE TRAVELING TIME vs. OTHER METHODS
#How to calculate Citibike times?
#Using the Google API and the Citibike API, we can first calculate the directions from current destination/start destination to the nearest Citibike dock
#Then use the distance from that dock to Citibike dock closest to destination
#Then calculate walking distance from that dock to destination
#Sum up all distances/time => Total time necessary
#This will require the usage of "Waypoints"
##GOOGLE API KEY
key = 'AIzaSyBun2m9jaQTFGb0qtR7Shh7inqFhzKbLL4' #API key

def citi_bike():
        url = "http://www.citibikenyc.com/stations/json"
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result) #dictionary of our results
        #print d
        execTime = d['executionTime'] #gets the time when program was run, keeping here in case we want to use that somewhere!
        #just for testing purposes...
	rlist = d['stationBeanList']
	for r in rlist:
		print r['stationName'] 

def google_maps():
        #start = "345%20Chambers%20Street%20NY"
        start = "345 Chambers Street NY"
        start = start.replace(" ", "%20")#replacing spaces with %20 because spaces in urls are wonky
        #print start
        #end = "85-34%2060th%20Drive%20Middle%20Village%20NY"
        end = "85-34 60th Drive Middle Village NY"
        end = end.replace(" ", "%20") #replacing spaces with %20 because spaces in urls are wonky
        #print end
        googleurl = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&key=%s" % (start, end, key)
        #print googleurl
        request = urllib2.urlopen(googleurl)
        results = request.read()
        gd = json.loads(results) #dictionary of results returned by google
        routes = gd['routes']
        #NOTE: routes is a value in the dictionary gd; it is also a list with one element if there are no alternatives given
        #legs is the zeroth element of the routes list... and is itself another list
        legs = routes[0]['legs']
        #distance is referrring to the dictionary 'distance' in the first element of the list legs (which is a dictionary itself and where once again, all our valuable info is)
        distance = legs[0]['distance']
        print distance['text'] #returns textual information about distance btwn two points
        #print distance['value']#distance in meters
        ##########################################################
        duration = legs[0]['duration']
        print duration['text'] #how long it takes --> defaulted to driving
        ###########################################################
        steps = legs[0]['steps'] #list of dictionaries, where each dict is a step
        for s in steps:
                print s['html_instructions']

if __name__ == '__main__':
        google_maps()
