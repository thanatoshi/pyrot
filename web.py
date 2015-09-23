import webbrowser

new = None

new = 2 
  
google = {'Google', 'google', 'Google.com', 'google.com'}
facebook =  {'Facebook', 'facebook', 'facebook.com', 'Facebook.com'}
reddit = {'reddit', 'Reddit', 'reddit.com', 'Reddit.com'}

url = raw_input('''
    URL in this format: http://www.URLGOESHERE.com/? ''')

if url in "google":
  webbrowser.open("http://www.google.com/",new=new)
  raw_input("Press [ENTER] to continue.")
if url in "facebook":
  webbrowser.open("http://www.facebook.com/",new=new)
  raw_input("Press [ENTER] to continue.")
if url in "reddit":
  webbrowser.open("http://www.reddit.com/",new=new)
  raw_input("Press [ENTER] to continue.")
    
else:
  webbrowser.open(url,new=new)
  print
  raw_input("Press [ENTER] to continue.")

execfile('backagain.py')


