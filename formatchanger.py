import os,sys
folder = 'D:/VishalBackup/Adi/yo'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.webm', '.mp4')
       output = os.rename(infilename, newname)

print("yo")
