maxChain = 0

for i in range(1000000):
    cur_chain = 0
    while(i>1):
        if(i%2==0):
            i//=2
        else:
            i = (3*i)+1
        cur_chain+=1
    maxChain = max(maxChain,cur_chain)
print(maxChain)