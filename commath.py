#complex math
import math
import cmath

mathe = None
v = None
w = None
x = None
y = None
z = None


print('''Complex math!
      
      What would you like to do?
      
      [P]owers/Roots
      [Q]uadratics
      
      ''')

power = {'p','P', 'powers', 'power', 'root', 'roots', 'Powers/Roots', 'powers/roots', 'Roots', 'Powers'}
quad = {'quad', 'Quad', 'q', 'Q', 'Quadratic', 'quadratic'}

mathe = raw_input("")

print
print

if mathe in power:
    print("This feature lists all powers and roots up to ten, for the number you put in.")
    print
    x = input("What number would you like a list of the powers and roots to? ")
    x0 = x**0
    x1 = x**1
    x2 = x**2
    x3 = x**3
    x4 = x**4
    x5 = x**5
    x6 = x**6
    x7 = x**7
    x8 = x**8
    x9 = x**9
    x10 = x**10
    print("The first column is which power, the second is the product.")
    print('0: '), x0
    print('1: '), x1
    print('2: '), x2
    print('3: '), x3
    print('4: '), x4
    print('5: '), x5
    print('6: '), x6
    print('7: '), x7
    print('8: '), x8
    print('9: '), x9
    print('10:'), x10
    print
    print
    print("Would you like the roots, too?")
    print
    
    confirm = None
    
    confirm = raw_input("Type 'Yes' to see the roots. Type 'No' to return to the original math menu. ")
    
    yes = {'yes', 'Yes'}
    no = {'no', 'No'}
    
    if confirm in yes:
        print("Roots coming your way!")
        print
        print
        p = 1 + .0
        x1 = x**1
        x2 = x**(p/2)
        x3 = x**(p/3)
        x4 = x**(p/4)
        x5 = x**(p/5)
        x6 = x**(p/6)
        x7 = x**(p/7)
        x8 = x**(p/8)
        x9 = x**(p/9)
        x10 = x**(p/10)
        print('0: '), x0
        print('1: '), x1
        print('2: '), x2
        print('3: '), x3
        print('4: '), x4
        print('5: '), x5
        print('6: '), x6
        print('7: '), x7
        print('8: '), x8
        print('9: '), x9
        print('10:'), x10
        raw_input('''
                  Press [ENTER] to continue...''')
        execfile("math.py")
    
    if confirm in no:
        print("Returning to the root menu.")
        print
        print
        print("Welcome back!")
        print
        execfile("math.py")
    
if mathe in quad:
    print('''This function solves quadratic equations for you!
          
          NOTE: Be sure to have it in this format beforehand:
          
          Ax^2 * Bx * C = 0
          ''')
    a = input("What is A? ")
    b = input("What is B? ")
    c = input("What is C? ")
    x = -(b) + cmath.sqrt((b**2) - (4*a*c))
    x1 = x/(2*a)
    print("X1 ="), x1
    y = -(b) - cmath.sqrt((b**2) - (4*a*c))
    x2 = y/(2*a)
    print("X2 ="), x2
    mathe = None
    raw_input('''
              Press [ENTER] to return to the mathematics menu...''')
    execfile('math.py')