import urllib2
import time

code = urllib2.urlopen("google.com")
pagesource = code.read()
print(pagesource)
