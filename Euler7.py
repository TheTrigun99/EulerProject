def isprime(nb):
    if nb==2: return True
    for i in range(2,int(math.sqrt(nb))+2):
        if nb%i==0:
            return False
    return True
def niemeprime(n):
    L=[]
    i=2
    while len(L)!=n:
        if isprime(i):
            L.append(i)
        i+=1
    return L[-1]
