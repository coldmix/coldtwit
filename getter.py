import json
import urllib2

url= "http://search.twitter.com/search.json?q=narendra+modi"
data = urllib2.urlopen(url)
jdata = json.load(data)

#print raw data 
print jdata