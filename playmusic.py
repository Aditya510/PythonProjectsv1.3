import requests
import time
import os
website_url = "http://" + input("PLease enter website root link")
print(website_url)
response = requests.get(website_url)
source_code = response.content
newsource = source_code
file = open("sourcecode.txt","w")
file.write(str(source_code))
file.close()
print("File printed")
checkcount = 0
while False:
      responseagain = requests.get(website_url)
      refreshedsource = responseagain.content
      if refreshedsource == newsource:
          checkcount += 1
          print("No change!")
          print("Number of times tried:",checkcount)
          time.sleep(300)
      elif refreshedsource != newsource:
          os.system("start C:/animals.mp3")
          print("Trying to play audio!")
          break


