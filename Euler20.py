def sumfactorial(n):
    if n==0:
        return 1
    a=n
    i=n
    while i!=1:
        i=i-1
        a=a*i
    s=str(a)
    sq=sum([int(i) for i in s])
    return sq
