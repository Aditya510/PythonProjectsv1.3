from google import search
count = 0
for url in search("greater noida college", stop=1000):
        string = "aboutgn"
        count+=1
        print(count)
        if string in url:
           break
print(count)

