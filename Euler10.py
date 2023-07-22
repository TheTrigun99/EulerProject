def sumnprime(n):#not optimized
    L=[]
    i=2
    while i<n:
        if isprime(i):
            L.append(i)
        i+=1
    s=0
    for j in L:
        s=s+j
    return s
