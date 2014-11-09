import urllib2
import json
import math
import googlemaps
##GOOGLE API KEY
key = 'AIzaSyBun2m9jaQTFGb0qtR7Shh7inqFhzKbLL4' #API key

#returns a list of dictionaries (each station is a dictionary)
def citi_list():
        url = "http://www.citibikenyc.com/stations/json"
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result) #dictionary of our results
        #print d
        execTime = d['executionTime'] #gets the time when program was run, keeping here in case we want to use that somewhere!.
	rlist = d['stationBeanList']
        return rlist

#given a specific location, will return the dictionary entry to the nearest citibike station        
def nearest_station(location):
        dis_list = []
        geo = googlemaps.geo_loc(location)
        for r in citi_list():#citi_list is a list of dictionaries
                geo_long = geo['lng']
                geo_lat = geo['lat']
                diff_long = geo_long - r['longitude']
                diff_lat = geo_lat - r['latitude']
                distance = math.sqrt((diff_long**2) + (diff_lat**2))
                dis_list.append(distance)
        print min(dis_list)
        min_ind = dis_list.index(min(dis_list))
        #print citi_list()[0]
        return citi_list()[min_ind]


if __name__ == '__main__':
        #print citi_list()
        print nearest_station("345 Chambers Street NY 10282")
