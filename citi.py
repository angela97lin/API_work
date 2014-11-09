import urllib2
import json

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
