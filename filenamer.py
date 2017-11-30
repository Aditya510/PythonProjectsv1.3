import os
path = 'C:/avaavaxvyy/'
directory = os.listdir(path)
for filename in directory:
    filepath = os.path.join(path, filename)
    print(filename)
    print(filepath)
    os.replace(filepath,filepath+".mp3")
    
