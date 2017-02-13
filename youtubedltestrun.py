import os
while True:
    link = input("Enter link: ")
    string = "youtube-dl --extract-audio --audio-format mp3 "
    string += link
    os.system(string)

    
