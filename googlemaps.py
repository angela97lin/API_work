import urllib2
import json

##GOOGLE API KEY
key = 'AIzaSyBun2m9jaQTFGb0qtR7Shh7inqFhzKbLL4' #API key

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
