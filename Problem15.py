# https://www.youtube.com/watch?v=M8BYckxI8_U

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def paths(n):
    nfact = fact(n*2)
    mfact = fact(n)**2
    print(nfact//(mfact))

paths(20)
