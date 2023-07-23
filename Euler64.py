def odcf(n):
    a0=int(math.sqrt(n))
    L=[a0]
    a=a0
    d=1.0
    m=0.0
    period=0
    if a0!=math.sqrt(n):
        while a!=2*a0:
            m=d*a-m
            d=(n-m**2)/d
            a=int((a0+m)/d)
            L.append(a)

    return len(L)-1,L
ct=0
for i in range(1,10001):
    if odcf(i)[0]%2==1:
        ct+=1
print(ct)
