import urllib2
import json

if __name__ == '__main__':
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
