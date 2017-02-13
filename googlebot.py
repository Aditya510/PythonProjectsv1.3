import urllib3, html2text
import requests

http = urllib3.PoolManager()
site='https://www.google.co.in/adgjjfg'
r = http.request('GET', site)
print(r.data)
f = requests.get(site)
data = f.text
print(data)
c = html2text.html2text(str(r.data))
print(c)