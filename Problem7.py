n = 10001

def primeth(n):
    primes = [2]
    attempt = 3
    while n>=len(primes):
        if all(attempt%prime!=0 for prime in primes):
            primes.append(attempt)
        attempt+=2
    print(primes[-1])

primeth(n)