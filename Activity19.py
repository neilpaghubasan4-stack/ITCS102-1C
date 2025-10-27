for x in range(1,11,1):
    for s in range(10,x,-1):
        print(" ",end=" ")
    for y in range(1,x,1):
        print("*",end=" ")
    for z in range(1,x,1):
        print("*",end=" ")
    print()
for a in range(1,11,1):
    for b in range(1,a,1):
        print(" ",end=" ")
    for c in range(10,a,-1):
        print("*",end=" ")
    for d in range(10,a,-1):
        print("*",end=" ")
    print()
