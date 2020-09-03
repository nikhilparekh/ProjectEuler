n = 100

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

num = str(fact(n))
res = sum([int(x) for x in num])
print(res)

    
    