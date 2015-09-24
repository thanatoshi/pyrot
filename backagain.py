print('''
Back again? Fantastic!

The time is''' + time.strftime(" %H:%M:%S (%I:%M:%S%p) on %A the %d, %B, %Y.") + '''
      What would you like me to do?, ''' + name + '''?

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