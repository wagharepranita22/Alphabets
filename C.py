n=int (input("Give your n th :"))
for i in range(n):
    for j in range(n):
        if((i == 0 or i == n-1) and (j != 0 and j != n-1)) or ((j == 0) and (i != 0 and i != n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()