def collatz(n):
    L=[n]
    a=n
    while a!=1:
        if a%2==0:
            a=a//2
            L.append(a)
        else:
            a=3*a+1
            L.append(a)
    return len(L)
def longestcollatz(n):
    m=0
    p=0
    for i in range(1,n):
        if collatz(i)>m:
            m=collatz(i)
            p=i
    return p
