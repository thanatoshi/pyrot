print('''
Back again? Fantastic!

What would you like me to do, ''' + name + '''?

  "M"ath
  "T"ell time
  "O"pen web

Please choose a letter that corresponds with your needs.
''')

math = {'M', 'm', 'Math', 'math', 'Mathematics', 'mathematics'}
time = {'t', 'T', 'Time', 'time'}
web = {'o', 'O', 'Open web', 'Open Web', 'open web', 'open Web', 'open', 'Open'}

need = None
need = raw_input()

if need in math:
  execfile("math.py")
if need in time:
    #time
	import time
	print(time.strftime("%H:%M:%S (%I:%M:%S%p) on %A the %d, %B, %Y."))
	print
	print("To check if it's day or night: LOOK OUTSIDE!")
	print
	raw_input("Press [ENTER] to continue.")
	need = None
	execfile("backagain.py")

if need in web:
  execfile('web.py')