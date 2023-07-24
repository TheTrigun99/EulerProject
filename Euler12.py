def divisor(n):
    ct=0
    for i in range(1,int(math.sqrt(n))+1):
        q,r=divmod(n,i)
        if r==0:
            ct+=1
            if i!=q:
                ct+=1

    return ct
def triangdiv(n):
    i=1
    trig=1
    while divisor(trig)<n:
        i=i+1
        trig=trig+i
    return trig
