#weather
need = (None)

print('''This function will produce for you the weather conditions for your area,
      according to Weather Underground. The next input will ask for your ZIP.''')

print

location = input("ZIP code? ")

import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/Your_Key/geolookup/conditions/q/IA/Cedar_Rapids.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()