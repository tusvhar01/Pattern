for i in range(1,4):
    for j in range(1,6):
        if (j>=4-i and j<=2+i):
            print("*",end='')
        else:
            print(" ",end='')
    print()