n = 20000000
add = 2
primes = [2]
attempt = 3
while(n>=add):
    if all(attempt%prime!=0 for prime in primes):
        primes.append(attempt)
        add+=attempt
    attempt+=2
print(add)