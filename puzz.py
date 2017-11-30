x = int(input("Please enter value")
persons = list(range(1,x)) # The question asks 1-indexing
while len(persons) > 1:
    for index, person in enumerate(persons):
        del persons[(index + 1) % len(persons)]

print(persons)
