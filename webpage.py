
import webbrowser
import os
import time
for i in range(10):
   webbrowser.open("https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=0ahUKEwi3tqWpuN_RAhUGTY8KHcC8DUI4MhAWCE8wCQ&url=http%3A%2F%2Fwww.aboutgn.com%2Fdetail1.php%3Fid%3D1079&usg=AFQjCNH-HU_xYts6lRn5Ria-21gZBsF-bA&bvm=bv.145063293,d.c2I")

time.sleep(20)
browserExe = "iexplore.exe"
os.system("taskkill /f /im "+browserExe)
print("Done")
