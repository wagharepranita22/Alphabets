n = int(input("give your n the :"))
for i in range(n):
    for j in range(n):
        if(j==0) or ((j == n-1) and  (i != 0 and i != n-1)) or ((i==0 or i == n-1) and (j < n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()