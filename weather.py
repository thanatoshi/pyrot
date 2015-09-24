#weather
need = (None)

print('''
This function will produce for you the weather conditions for your area,
according to Weather Underground. The next input will ask for your ZIP.''')

print

zip = input("   ZIP code? ")
print

import urllib2
import json
url = ("http://api.wunderground.com/api/b2d7a183c77895f0/geolookup/conditions/q/") + str(zip) +  (".json")
f = urllib2.urlopen(url)
json_string = f.read()
parsed_json = json.loads(json_string)
pj = parsed_json['current_observation']
loc = parsed_json['location']
city =  loc['city'] + ", " + loc['state']
#state = loc['state']
temp_f = pj['temp_f']
feels = pj['feelslike_f']
weather = pj['weather']
obtime = pj['observation_time']

#print("The temperature in %s, %s is: %s" % (location, state, temp_f) + ", feels like: %s" % (feels))
print("     The temperature in " + city + " is: %s" % (temp_f) + ", feels like: %s" % (feels))

print("     Current weather in " + city + " is: %s" % (weather) + '''.
      
      '''+ "[Note: %s" % (obtime) + "]")

raw_input('''
          press [ENTER] to continue...''')
f.close()
execfile('backagain.py')


