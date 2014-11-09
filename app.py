# Justin Strauss and Angela Lin
# Software Development Period 7
# API Project

from flask import Flask, render_template, request, redirect, session, url_for, flash
import urllib2, json, urllib

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
	if request.method=="POST":
		origin = request.form["origin"]
		destination = request.form["destination"]
#		print urllib.quote_plus(origin)
#		print urllib.quote_plus(destination)
		station1 = getClosest(origin)
		station2 = getClosest(destination)
		print station1
		print station2
		return render_template("result.html")
	else:
		return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

def getClosest(address):
# returns the latitude and longitude of the closest Citibike station to a given address
	stationList = getStations()
	#for latlong in stationlist:
	#	getDistance(address, latlong)
	distances = [getDistance(address, latlong, "walking") for latlong in stationList]
	shortest = min(distances)
	index = distances.index(shortest)
	return stationList[index]

def getStations():
# returns a list of the latitudes and longitudes of all Citibike stations in the system
	rlist = getCitiJSON()
	#stationlist = [r["stationName"] for r in rlist]
	stationList = [str(r["latitude"])+","+str(r["longitude"]) for r in rlist]
	return stationList

def getCitiJSON():
# returns a dictionary of Citibike station information
	url = "http://www.citibikenyc.com/stations/json"
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result)
	rlist = d['stationBeanList']
	return rlist

def getDistance(origin, destination, mode):
# returns the distance (in meters) between two locations given a mode of transportation
	rlist = getGoogleJSON(origin, destination, mode)
	if isinstance(rlist, basestring):
		return rlist
	else:
		return rlist['legs']['distance']['value']

def getGoogleJSON(origin, destination, mode):
# returns a dictionary of Google Map route information
	url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%s" % (origin, destination, mode)
	print url
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result)
	if d["status"]!="OK":
		return "No %s directions exist between %s and %s." %(mode, origin, destination)
	else:
		rlist = d['routes']
		return rlist

# @app.route('/authorize')
# def authorize():
# 	return

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
