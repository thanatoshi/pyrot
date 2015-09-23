#personal assistant v.000001
import webbrowser
import sys
import time
confirm = {'yes', 'Yes', 'Sure', 'sure'}

print("Hello world!")

print

name = raw_input("What is your name? ").title()

print('''
Greetings, ''' + name + '''! My name is Pyrot!

I am your own personal assistant, capable of calculating mathematical problems, telling you the time, and opening weblinks for you!
''')

print('''The time is''' + time.strftime(" %H:%M:%S (%I:%M:%S%p) on %A the %d, %B, %Y.") + '''
      What would you like me to do?

      "M"ath
      "C"heck Current Conditions/"W"eather
      "O"pen web


Please choose a option that corresponds with your needs.
''')

math = {'M', 'm', 'Math', 'math', 'Mathematics', 'mathematics'}
weather = {'w', 'W', 'weather', 'Weather', 'current conditions', 'Current Conditions', 'C', 'c', 'forecast', 'Forecast', 'Tell Time', 'tell Time'}
web = {'o', 'O', 'Open web', 'Open Web', 'open web', 'open Web', 'open', 'Open'}

need = raw_input()

if need in math:
  execfile('math.py')
if need in weather:
  execfile('weather.py')
if need in web:
  execfile('web.py')


