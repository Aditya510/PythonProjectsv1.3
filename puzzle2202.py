while True:
    d1 = int(input("Distance 1"))
    placed1 = 1000 - (2*d1)
    print(placed1)
    placed1 = placed1 - d1
    print(placed1)

    d2 = int(input("Distance 2"))
    placed2 = 1000 - (2*d2) - d1
    print(placed2)
    print(placed1 + placed2)
