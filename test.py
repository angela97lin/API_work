import urllib2
import json

if __name__ == '__main__':
	url = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&safe=on"
	url = url%("narwhal")
	request = urllib2.urlopen(url)
	result = request.read()
	d = json.loads(result)
	rlist = d['responseData']['results']
	for r in rlist:
		print r['titleNoFormatting']