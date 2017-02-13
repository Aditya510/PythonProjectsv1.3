import random
import urllib.requ

def imagedownload(url):
    x = random.randint(1,10)
    filenome = str(x) + ".jpg"
    urllib.request.urlretrieve(url,filenome)

imagedownload("http://i.telegraph.co.uk/multimedia/archive/03589/Wellcome_Image_Awa_3589699k.jpg")
