#sieve for primes
def primegen(n):
    y = list(range(1,n,2))
    print(y)
    fewprimes = [3,5]
    for ite in fewprimes:
        y = [item for item in y if item%ite != 0]
    print(y)

print(primegen(1000000))
