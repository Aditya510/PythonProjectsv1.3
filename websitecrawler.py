import urllib2

response = urllib2.urlopen("http://google.de")
page_source = response.read()
print(page_source)
