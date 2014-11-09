import urllib2
import json

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

#finds the longitude and latitude of a given location parameter using Google's Geocode API
#return format is a dictionary with longitude and latitude as keys
def geo_loc(location):
        location = location.replace(" ", "%20")
        #print location
        googleurl = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location,key)
        #print googleurl
        request = urllib2.urlopen(googleurl)
        results = request.read()
        gd = json.loads(results) #dictionary
        result_dic = gd['results'][0] #dictionary which is the first element in the results list
        #print result_dic
        geometry = result_dic['geometry'] #geometry is another dictionary
        #print geometry
        loc = geometry['location'] #yet another dictionary
        #print loc
        #longitude = loc['lng']
        #latitude = loc['lat']
        #print longitude
        #print latitude
        return loc



if __name__ == '__main__':
        print citi_dic()
