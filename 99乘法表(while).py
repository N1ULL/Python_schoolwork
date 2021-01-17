i=1
while i<10:
    j=1
    while j<=i:
        print("%d*%d=%2d"%(j,i,j*i),end=' ')
        j+=1
    print("")
    i+=1