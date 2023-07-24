def divisorlists(n):
    L=[]
    for i in range(1,int(math.sqrt(n))+1):
        q,r=divmod(n,i)
        if r==0:
            L.append(i)
            if i!=q and q!=n:
                L.append(q)

    return sum(L)

def amicalnbsum(n):
    s=0
    for i in range(n):
        p=divisorlists(i)
        if divisorlists(p)==i and i!=p:
            s=s+p
    return s
