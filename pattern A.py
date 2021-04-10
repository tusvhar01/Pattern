for row in range(1,8):
    for col in range(1,6):
        if ((row==1 or row==4) or ((col==1 or col==5) and (row!=1 and row!=4))) :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()