def powerSum(num,power):
    res = str(num**power)
    ans = [int(x) for x in res]
    print(sum(ans))

powerSum(2,15)
powerSum(2,1000)