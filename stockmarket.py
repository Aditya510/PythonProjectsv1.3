while True:
    import urllib3
    import html2text
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://getquote.icicidirect.com/trading_stock_quote.aspx?Symbol=JSWSTE')
    r = r.data
    r = str(r)
    text = html2text.html2text(r)
    print(text[975:988])
