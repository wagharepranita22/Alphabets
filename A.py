n = int(input("give your input :"))
for i in range(n):
    for j in range(n):
        if ((j == 0 or  j== n-1) and (i != 0)) or ((i == 0 or i == n//2) and (j > 0 and j < n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()