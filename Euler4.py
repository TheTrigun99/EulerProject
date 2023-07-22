def reverse_nb(n):
    nb=n
    re=0
    i=1
    while nb!=0:
        re=re*10+ nb%10
        nb=nb//10
    return re
def palindrome(n):
    nb=0
    for i in range(10**(n-1),10**n):
        for j in range(i,10**n):
            pp=i*j
            if pp==reverse_nb(pp) and pp>nb:
                nb=pp
    return nb
