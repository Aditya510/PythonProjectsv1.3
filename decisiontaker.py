import random
print("Enter things between which you want to make a decision")
xio = input()
decision = list(xio.split())
result = random.choice(decision)
print(result)
print("Welcome")
