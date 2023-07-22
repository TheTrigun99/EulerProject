def fibousum(limit):
    a,b=1,2
    s=0
    while b<limit:
        if b%2==0:
            s+=b
        a,b=b,a+b
    return s
