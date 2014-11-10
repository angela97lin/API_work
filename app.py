# Justin Strauss and Angela Lin
# Software Development Period 7
# API Project

from flask import Flask, render_template, request, redirect, session, url_for, flash
import urllib2, json, urllib, math
key = 'AIzaSyBun2m9jaQTFGb0qtR7Shh7inqFhzKbLL4'

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
	if request.method=="POST":
		# read form data
		origin = request.form["origin"]
		destination = request.form["destination"]

		# find the latitude and longitude of the stations closest to origin and destination
		station1 = closestStation(origin)
		station2 = closestStation(destination)
		latlong1 = str(station1["latitude"])+","+str(station1["longitude"])
		latlong2 = str(station2["latitude"])+","+str(station2["longitude"])

		# get dictionaries of Google Map route info for walking/bicycling
		rlist1 = getGoogleJSON(urllib.quote_plus(origin),latlong1,"walking")
		rlist2 = getGoogleJSON(latlong1,latlong2,"bicycling")
		rlist3 = getGoogleJSON(latlong2,urllib.quote_plus(destination), "walking")

		# flash error messages if a route doesn't exist
		flashed = False
		if isinstance(rlist1, basestring):
			flash(rlist1)
			flashed = True
		if isinstance(rlist3, basestring):
			flash(rlist3)
			flashed = True
		if flashed:
			return render_template("result.html")

		# use the dictionaries to get the distance for each leg of the Citibike trip
		d1 = rlist1[0]['legs'][0]['distance']['value']
		d2 = rlist2[0]['legs'][0]['distance']['value']
		d3 = rlist3[0]['legs'][0]['distance']['value']

		# flash error messages if the walk is too far
		if d1 > 1000:
			flash("Your origin is over a kilometer walk from the closest Citibike station.")
			flashed = True
		if d3 > 1000:
			flash("Your destination is over a kilometer walk from the closest Citibike station.")
			flashed = True
		if flashed:
			flash("Please use locations within the current Citibike Service area!")
			return render_template("result.html")

		# getDistance(origin, station1, "walking")
		# getDistance(station2, destination, "walking")
		# print station1
		# print station2
		return render_template("result.html", d1=d1, d2=d2, d3=d3)
	else:
		return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

def closestStation(address):
# returns the dictionary entry of the closest Citibike station to a given address
	geo = geo_loc(address)
	rlist = getCitiJSON()
	distances = [math.sqrt((geo['lng']-r['longitude'])**2 + (geo['lat']-r['latitude'])**2) for r in rlist]
	shortest = min(distances)
	index = distances.index(shortest)
	return rlist[index]

def geo_loc(location):
#finds the longitude and latitude of a given location parameter using Google's Geocode API
#return format is a dictionary with longitude and latitude as keys
	location = urllib.quote_plus(location)
	googleurl = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location,key)
	request = urllib2.urlopen(googleurl)
	results = request.read()
	gd = json.loads(results) #dictionary
	result_dic = gd['results'][0] #dictionary which is the first element in the results list
	geometry = result_dic['geometry'] #geometry is another dictionary
	loc = geometry['location'] #yet another dictionary
	return loc

def getCitiJSON():
# returns a dictionary of Citibike station information
	url = "http://www.citibikenyc.com/stations/json"
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result)
	rlist = d['stationBeanList']
	return rlist

def getGoogleJSON(origin, destination, mode):
# returns a dictionary of Google Map route information
	url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%s&key=%s" % (origin, destination, mode, key)
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result)
	if d['status'] != "OK":
		return "No %s directions exist between %s and %s." %(mode, origin, destination)
	else:
		rlist = d['routes']
		return rlist

if __name__ == '__main__':
	app.secret_key = "don't store this on github"
	app.debug = True
	app.run(host='0.0.0.0')
