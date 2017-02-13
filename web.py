import urllib3, html2text    #Domain Name availiblity checker.
def checkdomain(domain):
    http = urllib3.PoolManager()
    site='http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=' + domain + ".com"
    r = http.request('GET', site)
    c = html2text.html2text(str(r.data))
    tocheck = "has already been registered"
    if tocheck not in c:
        return True
    return False
    #for explicit usage, if tocheck in c:  print("Domain " + str(domain) + " not available.")  else:  print("Domain " + str(domain) + " available.")
results = []
consonants = "b c d f g h j k l m n p q r s t v w x y z"
vowels = "a e i o u"
consonants = consonants.split()        #Converting the string to a list.
vowels = vowels.split()
for j in range(200):
    string = ""
    for i in range(3):                 #Generate a random 6 letter word of the form CVCVCV
        string+= random.choice(consonants)
        string+= random.choice(vowels)
    if checkdomain(string):
        if string not in results:
            string.capitalize()
            string += ".com"
            results.append(string)
    if j == 100 : print("Half done")
file = open("domainname.txt", "w")     #opening the file to write.
results.sort()                         #sorting the results for ease of access.
for item in results:                   #iterating over every item to write it on the file.
    file.write(item)
    file.write("\n")
file.close()                           #closing the file.
print("Done")



# l1 = input("Enter first group of words").split()

# import random
# for i in l1:
#     for j in range(0,10):
#         stri = random.choice(consonants)
#         stri += random.choice(vowels)
#         stri += random.choice(vowels)
#         stri += random.choice(consonants)
#
#         s1 = i + stri
#         s2 = stri + i
#         if checkdomain(s1):
#             print(s1)
#         if checkdomain(s2):
#             print(s2)
# import random
# for item in (itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3)):
#     string = ""
#     for subitem in item:
#         string+= subitem
#     checkdomain(string)
#     ctime = time.time()
#     print(ctime-start)

