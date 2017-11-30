import youtube_dl
from subprocess import call
import threading
from multiprocessing import Process
def givecommand(command):
    call(command.split(), shell=False)
while True:
    link = input("Feed me the song please.")
    command = "youtube-dl -o ~D:/VishalBackup/Adi/DJ/%(title)s.%(ext)s --audio-format mp4 " + link
    #command = "youtube-dl -o ~D:/VishalBackup/Adi/DJ/%(title)s.%(ext)s --extract-audio --audio-format mp3 " + link
    t = threading.Thread(target=givecommand, args=(command,))
    t.start()
