myfile = open("firstfile.txt","w")
myfile.write("Let's try this thing out")
myfile.close()
readfile = open("firstfile.txt",'r')
re = readfile.read()
print(re)

