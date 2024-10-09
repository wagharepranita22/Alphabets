n = int (input("N :"))
for i in range(n):
    for j in range(n):
        if ((i == j) and (j < n//2)) or ((j+i == n-1) and (i < n//2)) or ((j == n//2) and (i >= n//2)) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
