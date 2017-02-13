import core
import urllib3
import html2text
import time
while True:
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://getquote.icicidirect.com/trading_stock_quote.aspx?Symbol=JSWSTE')
    r = r.data
    r = str(r)
    text = html2text.html2text(r)
    test1 = (text[978:984])

    test2 = text[982:988]
    try:
        result = float(test1)
    except:
        result = float(test2)

    print(result)
    #
    if result > 187:
        result = str(result)
        print("yahoo")
        core.respond('Current price is ' + result + ". You should sell your stock right now")
        core.speak()
    time.sleep(10)