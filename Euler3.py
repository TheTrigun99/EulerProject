def largestprim(n):
    nb=n
    i=2
    s=0
    while i*i<nb:
        while nb%i==0:
            nb=nb/i
        i=i+1
    return(nb)
