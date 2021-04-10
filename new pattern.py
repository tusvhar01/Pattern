for i in range(1,4):
    for j in range(1,7):
        if (j<=4-i or j>=3+i):
            print("*",end='')
        else:
            print(" ",end='')
    print()


