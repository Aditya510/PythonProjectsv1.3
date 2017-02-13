import os
directory = "D:\Vishal Back up\Adi\Mama songs - Copy"
for file in os.listdir("D:\Vishal Back up\Adi\Mama songs - Copy"):
    newfile = file + '.mp3'
    a = os.path.join(directory,file)
    b = os.path.join(directory,newfile)
    print(newfile)
    os.rename(a, b)

