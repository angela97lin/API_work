# Justin Strauss and Angela Lin
# Software Development Period 7
# API Project

from flask import Flask, render_template, request, redirect, session, url_for, flash
import urllib2
import json

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
	if request.method=="POST":
		origin = request.form["origin"]
		destination = request.form["destination"]
		station1 = getClosest(origin)
		station2 = getClosest(origin)
		return render_template("result.html")
	else:
		return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

def getClosest(address):
# returns the closest Citibike Station to a given address
	url = "http://www.citibikenyc.com/stations/json"
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result)
	rlist = d['stationBeanList']
	stationlist = [r["stationName"] for r in rlist]
	print stationlist
	return address

# @app.route('/authorize')
# def authorize():
# 	return

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
