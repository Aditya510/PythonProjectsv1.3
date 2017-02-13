import urllib3
import html2text
http = urllib3.PoolManager()
r = http.request('GET', 'http://m.cricbuzz.com/cricket-commentary/16947/ind-vs-ban-only-test-bangladesh-tour-of-india-2017')
c = r.data

a = html2text.html2text(str(c))
print(a[200:5000])

a = a[238:2200]
tag = a[:33]

string = tag[:3] +"IA score is currently " + tag[6:9] + " with loss of " + tag[10] + " wickets."
players = (a[100:300])


import core
core.respond(string)
core.speak()
