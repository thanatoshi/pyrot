#weather
need = (None)

print('''This function will produce for you the weather conditions for your area,
      according to Weather Underground. The next input will ask for your ZIP.''')

print

zip = input("ZIP code? ")

import urllib2
import json
url = ("http://api.wunderground.com/api/b2d7a183c77895f0/geolookup/conditions/q/") + str(zip) +  (".json")
f = urllib2.urlopen(url)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
feels = parsed_json['current_observation']['feelslike_f']
weather = parsed_json['current_observation']['weather']
obtime = parsed_json['current_observation']['observation_time']

print("The temperature in %s is: %s" % (location, temp_f) + ", feels like: %s" % (feels))

print("Current weather in %s is: %s" % (location, weather) + ".")
print
print("[Note: %s" % (obtime) + "]")

raw_input('''
          press [ENTER] to continue...''')
f.close()
execfile('backagain.py')


