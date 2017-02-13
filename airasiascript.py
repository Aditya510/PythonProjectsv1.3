url = "http://booking.airasia.com/Flight/Select?o1=DEL&d1=KUL&culture=en-GB&dd1=2017"

suffix = "&ADT=1&CHD=0&inl=0&s=true&mon=true&cc=INR&c=false"
import urllib3
import html2text
urllib3.disable_warnings()


for month in range(1,12):
    for day in range(1,30):
        base = "-"
        if month < 10:
            base += "0"
            base += str(month)
        else:
            base += str(month)
        base += "-"
        if day < 10:
            base += "0"
            base += str(day)
        else:
            base += str(day)
        http = urllib3.PoolManager()
        site = url + base + suffix
        r = http.request('GET', site)
        c = html2text.html2text(str(r.data))
        print(site)
        tocheck = "price"
        print(c)
        if tocheck in c:
            print("Yup")




