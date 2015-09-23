#math
import math
import cmath

print('''
What sort of math would you like to do, ''' + name + '''?

  "A"ddition
  "S"ubtraction
  "M"ultiplication
  "D"ivision

Don't type anything and just hit enter for more!
''')

need = None
mathe = raw_input("")
print

add = {'a', 'Addition', 'addition', 'A'}
sub = {'s', 'Subtraction', 'subtraction', 'S'}
mult = {'m', 'M', 'Multiplication', 'multiplication'}
div = {'d', 'D', 'Division', 'division'}

if mathe in add:
  #addition
  print('''You chose addition! How many numbers are going to be in this
  problem? (Choose a number, 2-5)''')
  
  numbers = input("")
  
  if numbers == 2:
    x = input("What is x? ")
    y = input("What is y? ")
    answer = (x+y)
    print
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    
    execfile("backagain.py")
  
  if numbers == 3:
    x = input("What is x? ")
    y = input("What is y? ")
    z = input("What is z? ")
    answer = (x+y+z)
    print
    print str('The answer is'), answer
    print
    raw_input("Press [ENTER] to go back to the menu. CTRL+C to end it.")
    execfile("backagain.py")
    
  if numbers == 4:
    w = input("What is w? ")
    x = input("What is x? ")
    y = input("What is y? ")
    z = input("What is z? ")
    answer = (w+x+y+z)
    print('''''')
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    execfile("backagain.py")
    
  if numbers == 5:
    v = input("What is v? ")
    w = input("What is w? ")
    x = input("What is x? ")
    y = input("What is y? ")
    z = input("What is z? ")
    answer = (v+w+x+y+z)
    print('''''')
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    execfile("backagain.py")

elif mathe in sub:
  print('''You chose subtraction! How many numbers are going to be in this
  problem? (Choose a number, 2-5)
  
  Remember, put numbers in the order they're to be subtracted!
  ''')
  
  numbers = input("")
  
  if numbers == 2:
    x = input("What is x? ")
    y = input("What is y? ")
    answer = (x-y)
    print
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    execfile("backagain.py")
  
  if numbers == 3:
    x = input("What is x? ")
    y = input("What is y? ")
    z = input("What is z? ")
    answer = (x-y-z)
    print
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    execfile("backagain.py")
  if numbers == 4:
    w = input("What is w? ")
    x = input("What is x? ")
    y = input("What is y? ")
    z = input("What is z? ")
    answer = (w-x-y-z)
    print
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    execfile("backagain.py")
  if numbers == 5:
    v = input("What is v? ")
    w = input("What is w? ")
    x = input("What is x? ")
    y = input("What is y? ")
    z = input("What is z? ")
    answer = (v-w-x-y-z)
    print
    print str('The answer is'), answer
    raw_input("Press [ENTER] to continue. CTRL+C to end it.")
    execfile("backagain.py")
    
elif mathe in mult:
  
    print("You chose multiplication!")
    print
    
    x = input("What is x? ")
    y = input("What is y? ")
    
    mor = raw_input("Is there another number? ")
    
    if mor in confirm:
      z = input("What is z? ")
      answer = (x*y*z)
      print str('The answer is'), answer
      raw_input("Press [ENTER] to continue. CTRL+C to end it.")
      execfile("backagain.py")
      
    else:
      answer = (x*y)
      print
      print str('The answer is'), answer
      print
      raw_input("Press [ENTER] to continue. CTRL+C to end it.")
      execfile("backagain.py")

elif mathe in div:
  print("You chose division!")
  print
  
  x1 = input("What is x? ")
  y1 = input("What is y? ")
  x = x1 + .0
  y = y1 + .0
  answer = (x/y)
  print
  print("The answer is"), answer
  print
  raw_input("Press [ENTER] to continue. CTRL+C to end it.")
  execfile("backagain.py")

else:
  print("Loading complex number program.. press [ENTER] to continue.")
  raw_input("")
  
  execfile("commath.py")