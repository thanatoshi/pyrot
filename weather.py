#weather
need = (None)

print('''This function will produce for you the weather conditions for your area,
      according to Weather Underground. The next input will ask for your ZIP.''')

print

zip = input("ZIP code? ")

import urllib2
import json
url = ("http://api.wunderground.com/api/b2d7a183c77895f0/geolocation/geolookup/conditions/q/") + str(zip) +  (".json")
f = urllib2.urlopen(url)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']

print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
