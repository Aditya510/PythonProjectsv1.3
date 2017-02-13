from google import search
count = 0
for url in search("greater noida", stop=100):
        string = "agoda"
        count+=1
        if string in url:
            break
print(count)
count = count % 10
count -= 1
print(count)
count *= 10

print(count)

import webbrowser
webbrowser.open("https://www.google.co.in/?gfe_rd=cr&ei=hoqJWNDAFe_s8AfFv5TgBw&gws_rd=ssl#q=greater+noida&start=" + str(count))
