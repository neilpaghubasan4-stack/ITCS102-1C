for x in range(1,11,1):
    for x in range(10,x,-1):
        print("@",end=" ")
    for y in range(1,x,1):
        print("#",end=" ")
    print()
