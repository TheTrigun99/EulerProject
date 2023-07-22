def squares(n):
    s=n*(n+1)*(2*n+1)//6
    sq=(n*(n+1)//2)**2
    return sq-s
