import urllib2
import json
import googlemaps
import citi

###The Directions API may only be used in conjunction with displaying results on a Google map; using Directions data without displaying a map for which directions data was requested is prohibited.

##COMPARING CITI-BIKE TRAVELING TIME vs. OTHER METHODS
#How to calculate Citibike times?
#Using the Google API and the Citibike API, we can first calculate the directions from current destination/start destination to the nearest Citibike dock
#Then use the distance from that dock to Citibike dock closest to destination
#Then calculate walking distance from that dock to destination
#Sum up all distances/time => Total time necessary
#This will require the usage of "Waypoints"


if __name__ == '__main__':
	googlemap.google_maps()
	print citi.geo_loc("345 Chambers Street 10282 NY")
