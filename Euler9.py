for i in range(1000):
    for j in range(i,1000):
        c=math.sqrt(i**2+j**2)
        if i+j+c==1000:
            print(i*j*c)
          
